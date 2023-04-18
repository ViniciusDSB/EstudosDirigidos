import math

#função do decaimento
def f(x):
    y = math.e**(-x)
    return y

def trapezio(a, b, m):
    x = a
    h = (b-a)/m
    I = 0
    for i in range(m):
        I+=(f(x)+f(x+h))
        x+=h
    return (h/2)*I


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
