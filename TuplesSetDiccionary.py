#una dupla se pone con parentesis 
t=(1,2,3,4) #estas ya no se pueden modificar 
#t.append(5)
#t[1]=40
print(t[1:4])   #imprime (2,3,4)
print (t[-1])

#para recorre duplas 
for i in t: 
    print (i)

#converti una dupla a una lista 
l=list(t)
#Agregar a la lista 
l.append(5)
print (l)
t2=tuple(l)
l.pop()  #Borra el ultimo elemento 
l.remove(2)
del l[2]
print(type(t))
print(type(l))     #Imprime los tipos de dato 
print(type(t2))


#CONJUNTO ENTRE LLAVES
#DUPLAS EN 
Programa = {'JUAN','MARIA','ESTEFANY', 'Lalo'}
Calculo={'Santiago', 'Lalo'}
Programa.add('Edu')
#Como borro un elemento del conjunto 
Programa.remove('JUAN')
#Programa.clear()
#Union de dos conjuntos 
C2=Programa & Calculo    # / union     & interccion    - diferencia 
print (C2)

print(Programa)
print(Calculo)
print ('MARIA' in Programa)    #Asi se pregunta en los conjuntos


#Diccionario (json)
#key, value
animales={'nombre':'Perro',
           'edad':'12',
           'pedigri':'CC0'}
animales2={'nombre':'Perro',
           'edad':'12',
           'pedigri':'CC0'}
animal=[animales,animales2,a3]

for a in animal: 
    print('{:<10s}{:<5d}{:<10s}'.format(a['nombre'],a['edad']))


"""
print(len(animales))
#agregar un valor al indice
animales['talla']='grande'
print(animales['nombre'])   #me imprime lo que hay en el diccionario animales
print(animales.get('pedigri'))
print(animales.get('talla'))

#imprime los valores
for d in animales:
   print(animales[d])

print (animales.values()) ##
print (animales.keys())
print (animales.items()) ##lista de tuplas

"""