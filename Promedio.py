#Lea n calificaciones y calcular el promedio. 
#Imprima la calificacion mas alta 
i=1
n=int(input('Numero de Alumnos: '))
s=0
m=0
while i<=n:
   c=int(input('Dame las calificaciones: '))
   if c>m:
       m=c
   s=s+c
   i+=1

prom=s/n
#print('El promedio es: ',prom)
print('El promedio es: %.2f\n Y la calificacion mayor es:%d'%(prom,m))
print(type(c))      #Tipo de variable
print(type(prom))