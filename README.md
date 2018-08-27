# Controle de quadricóptero por Inteligência Artificial


## Contexto
O presente projeto foi aprovado pelo curso de [Machine Learning Nanodegree Engineer](https://br.udacity.com/course/machine-learning-engineer-nanodegree--nd009) da Udacity. Parte do código-fonte, metodologia e modelo matemático é original desse curso. Portanto, cópia de parte do material é restrito e deve obrigatoriamente conter referência ao presente repositório.

## Quadricóptero
![Parrot AR Drone](https://s3.amazonaws.com/video.udacity-data.com/topher/2017/October/59d7c61e_parrot-ar-drone/parrot-ar-drone.jpg)
###### fonte: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:81RNYV29HCL._SL1500_%281/%29.jpg); [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

O *drone* é um Parrot AR Drone com 4 rotores com controles independentes. Aprender a controlar cada rotor coordenadamente para executar um padrão de voo não é intuitivo e, por isso, exigiria muito tempo de treinamento do piloto.

## Projeto
A proposta geral do projeto é criar um piloto automático que controle os 4 rotores de forma que o quadricóptero voe conforme a tarefa designada por um piloto não-treinado. Entretanto, a versão atual do projeto inclui apenas a tarefa de pairar imóvel na posição atual no início do comando.

## Piloto Automático
O piloto automático (*autopilot*) é uma Inteligência Artificial - IA (*Artificial Intelligence*) que foi treinada executando centenas de voos em simulação. A IA, também chamada de agente, possui redes neurais que são retreinadas a cada passo em cada voo considerando o grau de sucesso (ou fracasso) dos voos anteriores. Devido ao fato de se apoiar numa medida de sucesso, esse algoritmo de Aprendizado de Máquina (*Machine Learning*) é chamado de "Aprendizado por Reforço" (*Reinforcement Learning*). Além disso, também é chamado de "Aprendizado Profundo" (*Deep Learning*) pelo fato de usar redes neurais profundas. O nome do modelo matemático utilizado é *Deep Deterministic Policy Gradients* (DDPG) e seus detalhes estão documentados [nesse paper](https://arxiv.org/abs/1509.02971). 

## Código-Fonte
O arquivo principal onde a IA é criada e treinada está no `Quadcopter_AI_pilot.ipynb`. Ele deve ser acessado através do programa [Jupyter Notebook](http://jupyter.org/). Nele estão contidos os código-fontes e comentários mais detalhados sobre os passos do algoritmo.

O arquivo principal utiliza também outros arquivos na estrutura de pastas do repositório. Eles foram escritos em Python v3.x e utilizam as seguintes bibliotecas: keras, matplotlib, numpy e outras nativas do Pyhton.

## Resultado
A IA aprendeu corretamente a executar a tarefa de plainar imóvel na posição do início do comando, conforme evidenciado na figura abaixo. Portanto, é possível que outras tarefas também possam ser treinadas (ex: pousar, decolar, seguir um ponto móvel, etc).
![Melhor Voo](https://github.com/diogodutra/quad_AI/blob/master/best_flight.png)



## Rights
This project was submitted by Diogo Dutra as part of the Machine Learning Engineer Nanodegree At Udacity. As part of Udacity Honor code, your submissions must be your own work, hence submitting this project as yours will cause you to break the Udacity Honor Code and the suspension of your account.

Reference to this source is required whenever parts or the whole of the material
is used.

Standard license is applicable and this license notice must be included in all works derived from this project.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
