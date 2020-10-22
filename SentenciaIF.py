
edad=20

condicion = edad >=18
print(condicion)

if condicion:
    print('Ya Puedes votar')      #pass sirve para pasar a la siguiente condicion
else:
  print('No puedes votar, menor de edad')

#Operadores logicos 
#and, or, not

#Para optimiar el programa 
#if, if-else, elif
num=int(input('Dame numero: '))
if num>=0 and num<=10:
   print('Rango 0 al 10')
elif num>10 and num<=20: 
    print('Rango 11 al 20')
elif num>20 and num <=30:
    print('Rango 21 al 30')
else: 
    print('FUERA DE RANGO')

print('Programa terminado')

