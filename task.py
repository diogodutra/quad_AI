import numpy as np
from physics_sim import PhysicsSim
from math import log10

class Task():
    """Task (environment) that defines the goal and provides feedback to the agent."""
    def __init__(self, init_pose=None, init_velocities=None, 
        init_angle_velocities=None, runtime=5., target_pos=None):
        """Initialize a Task object.
        Params
        ======
            init_pose: initial position of the quadcopter in (x,y,z) dimensions and the Euler angles
            init_velocities: initial velocity of the quadcopter in (x,y,z) dimensions
            init_angle_velocities: initial radians/second for each of the three Euler angles
            runtime: time limit for each episode
            target_pos: target/goal (x,y,z) position for the agent
        """
        # Simulation
        self.sim = PhysicsSim(init_pose, init_velocities, init_angle_velocities, runtime) 
        self.action_repeat = 3

        #self.state_size = self.action_repeat * 6
        state = self.get_state()
        self.state_size = self.action_repeat * state.shape[0]
        self.action_low = 0
        self.action_high = 900
        self.action_size = 4

        # Goal
        self.target_pos = target_pos if target_pos is not None else np.array([0., 0., 10.]) 

    def get_reward(self):
        """Uses current pose of sim to return reward."""
        reward = 1.
        
        reward -= 0.3*(abs(self.sim.pose[:3] - self.target_pos)).sum() #punishes wrong position
        reward -= 0.1*(abs(self.sim.v)).sum() #punishes non-static state
        reward -= 1.1*(abs(self.sim.angular_v)).sum() #punishes rotational state
        
        #reward -= 1.3*abs(self.sim.pose[2] - self.target_pos[2]) #punishes wrong position
        #reward -= 1.1*abs(self.sim.v[2]) #punishes non-static state
        #reward -= 1.1*abs(self.sim.angular_v[1]) #punishes rotating state
        
        return reward

    def step(self, rotor_speeds):
        """Uses action to obtain next state, reward, done."""
        reward = 0
        pose_all = []
        for _ in range(self.action_repeat):
            done = self.sim.next_timestep(rotor_speeds) # update the sim pose and velocities
            reward += self.get_reward() / self.action_repeat
            #pose_all.append(self.sim.pose)
            state = self.get_state()
            pose_all.append(state)
        next_state = np.concatenate(pose_all)
        return next_state, reward, done

    def reset(self):
        """Reset the sim to start a new episode."""
        self.sim.reset()
        #state = np.concatenate([self.sim.pose] * self.action_repeat) 
        state = self.get_state()
        state = np.concatenate([state] * self.action_repeat) 
        return state
    
    def get_state(self):
        return self.sim.pose
