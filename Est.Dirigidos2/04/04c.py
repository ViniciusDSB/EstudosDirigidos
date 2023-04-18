import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from Modulo4 import f

a = 0
b = 1
m = 1000        #numero de iterações e também quão divido é o intervalo b-a
N = []          #numero de particulas em função do tempo
t = []          #valores de t para os quais o grafico N(t) sera plotado
x = a           #nde começa o eixo x
dx = (b-a)/m    #variação de x

for i in range(m):
    t.append(x)     #adiciona os pontos a serem mostrados no eixo de tempo/eixo x
    N.append(f(x))  #calcula o valor da função e adiciona os pontos a serem plotados no eixo N/eixo y

    x+=dx

plt.plot(t, N)
plt.xlabel('Time')
plt.ylabel('Particles')
plt.show()