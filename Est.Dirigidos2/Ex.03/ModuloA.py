import math
def f(x):
    y = math.e**x
    return y

#Calcula com a regr do trapézio
#h é o eixo delta x
#divide h pelo numero de interavalos
#B e b são as funçoes em h0 e h1 
#dai usa a formula da area do trapezio

def trapezio(a, b, m):
    x = a
    h = (b-a)/m
    I = 0
    for i in range(m):
        I+=(f(x)+f(x+h))
        x+=h
    return (h/2)*I



#calcula com a regra 1/3 de simpson
def simpson(a, b, m):
    x = a
    h = (b-a)/m

    I = f(a) + f(b)
    fator = 4

    for i in range(m-2):
        if fator == 4:
            x+=h
            I+= fator*f(x)
            fator = 2
        else:
            x+=h
            I+= fator*f(x)
            fator = 4
    return I*(h/3)
