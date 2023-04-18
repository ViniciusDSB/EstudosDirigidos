X = [-1, 0, 1, 2, 3]
Y = [1, 1, 0, -1, 2]

a = X[0]
b = X[len(X)-1]

h = (b-a)/len(X)

It = []
Is= []


#mostrar expressão com a regra dos trapezios
def trapezio():
    for i in range(len(X)):
        It.append(f'f({X[i]})')
    return It
print(f'I = {h}/2[{ " + ".join(trapezio()) }]')

#calcular valor da integral
I = 0
for i in range(len(X)):
        I+=(h/2)*Y[i]
print(f'I = {I:.3f}')


n = 0
miolo = ''
while(n<len(X)-2):
    n+=1
    if n%2==0:
        miolo+= f'2*{Y[n]} +'
    else:
        miolo+= f'4*{Y[n]} +'
     
print(f'I = {(h/3):.3f}*({Y[0]} + {miolo} {Y[len(Y)-1]})')
print('I = ', eval(f'{(h/3):.3f}*({Y[0]} + {miolo} {Y[len(Y)-1]})'))
