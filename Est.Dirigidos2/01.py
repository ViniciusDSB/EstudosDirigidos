m = 6
a = 0
b = 4
h = b-a

InTrapezio = []

#mostrar por trapezio para m iterações
def trapezio(m):

    if m%2==0:

        for i in range(m):
            InTrapezio.append(f'{h}/2(x{i}+x{i+1})')
        return '+'.join(InTrapezio)
    
    else:
        return 'Precisa ter m par'

print(trapezio(m))

InSimpson= []
def simpson(m):
    if m%2==0:
        InSimpson.append(f'{h}/3( f(x0) + f(x{m}) )')
        fator = 4
        for i in range(m-2):
            if fator == 4:
                InSimpson.append(f'{fator}(f(x{i+1}))')
                fator = 2
            else:
                InSimpson.append(f'{fator}(f(x{i+1}))')
                fator = 4
        return '+'.join(InSimpson)
    else:
        return 'Precisa de m par'

print(simpson(m))