"""
i=1
num=[]
while i<=10; 
  num.appends(i)
  i+=1
  """


"""
lista=[1,2,3],[4,5,6],[7,8,9]
print (lista)
"""
"""
#Crear una lista de listas 
l3=[[[4,78,3]],[2,4,5]]
print (l3[0][1][0])


"""
#llenar una lista 
lista=[]
r=int(input('Dame renglon: '))
c=int(input('Dame columna: '))

for i in range(0,r): 
  lista.append([])
  for j in range(0,c):
    lista[i].append(int(input('Dame numero: ')))
    #append agregar el ultimo elemento a la lista 
        

for i in lista:
  for j in i: 
    #print (j, end='')
    print("{0:<5}".format(j),end='')    #Manera en como se escribe <5 son los espacions entre la matriz
  print ()

"""
for i in range(0,len(lista)): 
    forj in range(o,lend(lista[i])):
       print(lista[i][j],end='')
    print()
"""    