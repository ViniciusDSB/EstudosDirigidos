from ModuloA import trapezio
from ModuloA import simpson

#Respostas da 03 - a)
print(trapezio(0, 1, 10))
print(simpson(0, 1, 10))

#Agora 03 - c)
#erro do trapezio
errT =  abs(( trapezio(0, 1, 1000)-trapezio(0, 1, 100) )/trapezio(0, 1, 100))
print("Erro relativo pelo trapezio:", errT)

errS = abs( ( simpson(0, 1, 1000)-simpson(0, 1, 100) )/simpson(0, 1, 100) )
print("Erro relativo pelo simpson:", errS)