
"""
n=1
while n<=5:
    print('Mensaje')
    n=n+1
for n in range(2,10,2):  #Se refleja la numaracion....
    print (n,'Mensaje')

"""
import math

opc='si'
while opc == "si":
    print('Programa de una ecuacion cuadratica')
    a=int(input('Digita el valor de a: '))
    b=int(input('Digita el valor de b: '))
    c=int(input('Digita el valor de c: '))

    if a!=0: 

     d= b**2-4*a*c
    if d>=0:
        x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
        x2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
        print('El resultado en X1:',x1)
        print('El resultado en X2:',x2)
    else:
        print('Solucion compleja')
    #else:
      #print('ERROR')
    opc = input('Desea la solucion de otra ecuacion')

print('Continua')