import math
import os

opc=0
while opc !=5:
    os.system('cls')
    print ('MENU PRINCIPAL')
    print('1. Area Triangulo')
    print('2. Salario Trabajador')
    print("3. Ecuacion Cuadratica")
    print('4. Edad')
    print('5. Salida')

    opc = int (input('Dame una opcion: '))

    if opc == 1: 
        print('Programa que calcule el area de un triangulo con los lados')

        a=int(input('Dame el lado A: '))
        b=int(input('Dame el lado B: '))
        c=int(input('Dame el lado C: '))
        print('Los valores ingresados son: ',a,b,c)
        s=(a+b+c)/2
        r=math.sqrt(s*(s-a)*(s-b)*(s-c))
        print('El area es: %.2f '%r)
    elif opc == 2:
        print('Programa que de el salario de un empleado')
        nombre = input('Nombre:')
        ht = int(input('Horas de trabajo: '))
        ph = float(input('Pago por hora: '))

        salario = ht*ph
        print('El salario del empleado:', salario)
    elif opc == 3:
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

        print('Continua')
    elif opc == 4: 
        edad=int(input('Dame tu edad: '))

        condicion = edad >=18
        print(condicion)
        if condicion:
         print('Ya Puedes votar')      #pass sirve para pasar a la siguiente condicion
        else:
         print('No puedes votar, menor de edad')
    elif opc == 5:
        print ('Gracias fue un placer')
    input('teclea')
