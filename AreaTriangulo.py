import math

print('Programa que calcule el area de un triangulo con los lados')

a=int(input('Dame el lado A: '))
b=int(input('Dame el lado B: '))
c=int(input('Dame el lado C: '))

print('Los valores ingresados son: ',a,b,c)

#Operador Aritmetico +,-,*,/,//,%**  la doble diagonal divide
#OR: >,<,<=,>=,==,!=
#OL: and, or, not
#OE

s=(a+b+c)/2
r=math.sqrt(s*(s-a)*(s-b)*(s-c))
print('El area es: %.2f '%r)   #Los porcientos ayudan a solo imprimir cierta cantidad de decimales. 

"""
print(7//3) imprime la parte entrea si solo le pongo uno me da los decimale. 
"""