menu="""
    MENU (CRUD)
    1.Altas (C)
    2.Bajas (D)
    3.Consultas (R)
    4.Modificacion (U)
    5.Reportes(R)
    6.Salir
    """

opc= None
nombre=[]
edades=[]
carreras=[]
promedio=[]
while opc !=6: 
  print(menu)
  opc=int(input('Dame una opcion: '))

  if opc == 1:
    nombre.append(input('Nombre: '))
    edades.append(int(input('Edad: ')))
    carreras.append(input('Carrera: '))
    promedio.append(float(input('Edad: ')))
  elif opc==2: 
    pass
  elif opc==3: 
    pass
  elif opc==4: 
    pass
  elif opc==5: 
    for i in range(0,len(nombre)): 
      print ('{:10s}{:<5')
  elif opc==6: 
    pass

