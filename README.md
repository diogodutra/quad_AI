# quad_AI
Reinforcement Learning agent that learns how to steadily hover a quadcopter.

Projeto de controle de um quadricóptero por Inteligência Artificial.

## Contexto
O trabalho é resultado de um dos projetos do curso de [Machine Learning Nanodegree Engineer](https://br.udacity.com/course/machine-learning-engineer-nanodegree--nd009) da Udacity. Portanto, parte do código-fonte, metodologia e modelo matemático é original da referência.

## Quadricóptero
![Parrot AR Drone](https://s3.amazonaws.com/video.udacity-data.com/topher/2017/October/59d7c61e_parrot-ar-drone/parrot-ar-drone.jpg)
(source: (Wikimedia Commons)[https://commons.wikimedia.org/wiki/File:81RNYV29HCL._SL1500_%281/%29.jpg]; [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/))

O drone é um Parrot AR Drone com 4 rotores com controles independentes. Controlar os rotores separadamente seria uma tarefa não-intuitiva e, por isso, exigiria muito tempo de aprendizado do piloto.

## Projeto
A proposta geral do projeto é criar um piloto automático que controle os 4 rotores de forma que o quadricóptero voe conforme a tarefa designada por um piloto não-treinado. Entretatno, a versão atual do projeto inclui apenas a tarefa de pairar imóvel na posição atual no início do comando.

## Piloto Automático
o piloto automático, também chamado de autopiloto, é uma Inteligência Artificial (IA) que foi treinada por Aprendizado de Máquina executando centenas de voos por simulação. A IA, também chamada de agente, possui redes neurais profundas que são retroalimentadas a cada passo de cada voo. Portanto, é do tipo "Aprendizado por Reforço". O nome do modelo matemático utilizado é *Deep Deterministic Policy Gradients* (DDPG) e detalhes estão documentados [nesse paper](https://arxiv.org/abs/1509.02971).

 

em inglês
