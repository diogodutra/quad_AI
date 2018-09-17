# Artificial Intelligence for Quadcopter Autopilot


## Context
The present project was approved by the [Machine Learning Nanodegree Engineer](https://br.udacity.com/course/machine-learning-engineer-nanodegree--nd009) course from Udacity. Part of the source code, methodology and mathematical model is original from this course. Therefore, copies of part of the material is restrict and they must contain reference to the present repository.

## Quadricopter
![Parrot AR Drone](https://s3.amazonaws.com/video.udacity-data.com/topher/2017/October/59d7c61e_parrot-ar-drone/parrot-ar-drone.jpg)
###### source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:81RNYV29HCL._SL1500_%281/%29.jpg); [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

The quadcopter is a Parrot AR Drone propelled by 4 rotors with independent controls. Learning to control each rotor with proper coordination to perform a predetermined flight pattern is not intuitive so it requires a long training from the pilot.

## Project
The general proposal is to design an autopilot to control the 4 rotors in order to perform a task designated by an untrained pilot. However, the last commit includes only the task to hover still at the target position.

## Autopilot
The autopilot is an Artificial Intelligence (AI) trained after hundreds of simulated flights.

The AI, also called agent, has neural networks that were repeatedly trained after every step considering the score of every flight. For this reason, this "Machine Learning" algorithm is also called "Reinforcement Learning". Moreover, it is also called "Deep Learning" due to the fact that a deep neural network was employed. The mathematical model used is the *Deep Deterministic Policy Gradients* (DDPG), as detailed in [this paper](https://arxiv.org/abs/1509.02971). 

## Souce code
The main file where the AI has been created and trained is the `Quadcopter_AI_pilot.ipynb`. It should be opened through the [Jupyter Notebook](http://jupyter.org/). Its code is properly commented with highlights about the algorithm.

The main file calls other files that are present in the repository folder structure. They were written for Python v3.x and they import the following libraries: keras, matplotlib, pandas, numpy and other natives from Python.

## Result
The AI has successfully learned to steadily hover at the same position from the beginning of the command, as ilustrated in the figure below. For this reason, it is possible that the AI can be trained to perform other flight patterns such as landing, taking off, following a moving target and others.
![Best flight](https://github.com/diogodutra/quad_AI/blob/master/best_flight.png)
###### IS measurements: seconds, meters, meters per second, radians, radians per second, rotations per second (reward is adimensional).




## *Rights*
*This project was submitted by Diogo Dutra as part of the Machine Learning Engineer Nanodegree At Udacity. As part of the Udacity Honor code, your submissions must be your own work, hence submitting this project as yours will cause you to break the Udacity Honor Code and the suspension of your account.*

*Reference to this source is required whenever parts or the whole of the material is used.*

*Standard license is applicable.*

*THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.*
