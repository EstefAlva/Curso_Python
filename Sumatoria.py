#Sumatoria de 1+2+3+4+5+...+n
#n=3, s=6
#n=5, s=15

#Declaracion de variables
"""
i=1
s=0
n=int(input('Dame un valor:'))
while i<=n:
   s=s+i 
   i+=1
"""
n=int(input('Dame un valor:'))
s=0
for i in range(1,n+1):
    s=s+i
print('Sumatoria es: ',s)