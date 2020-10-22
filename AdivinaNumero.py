#Adivinar un numero a la computadora
#Que numero estoy pensando

import  random
num=random.randint(1,10)
i=1
while i<=3:
    n=int(input('Adivina el numero que pense?'))
    if n==num: 
      print ('Adivinaste')
      break
    elif n<num:
       print('El numero es Mayor')
    else: 
        print('El numero es Menor')
    i+=1
if i!=3:
  print ('El numero que pense fue: ',num)