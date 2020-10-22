#Lista: Unidimencional, Bidimencional, Tridi, Multi

x=[1,2,500,4]
nombre = [1,4,56, True,[1,2,3],'Aldo', 'Estefany', 'Paco', 'Violeta', 'Carlos']

m=[[1,2,3],[4,5,6],[7,8,9]]
print(m[1][1])


print (nombre)
print(nombre[4])
#print(type(x))
print(x)

print(len(nombre))    #
print(nombre[0:6])
print(nombre[:6])
print(nombre[4:11])
print(nombre[4:])
print(nombre[0:12:2])
#print (nombre[1:5])
#print(nombre[3][2])

nombre.append('Juan')    #Agrega elementos 
nombre.extend([1,2,3])   #Agregar otra lista
nombre.pop(3)
print(nombre)


#Como crear una dupla
noms =('Juan','Maria')    #No se pueden cambiar los valores 
print (noms)

#Listas (mutables,indices)
#Tuplas (inmutables, indices)
#Conjuntos (no indices)
#Diccionarios (no indices)