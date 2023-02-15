#Crenado diccionarios en python
persona= {
    'nombre':"Santiago C",
    'edad':20,
    'estatura':1.83,
    'yaDesayuno': True,
    'equiposFavoritos':['Medellin','RiverPlate','Real Madrid','Liverpool']
}

#Creando diccionario vacio
ciudad={}

#acceder a un diccionario
print (persona)
print (ciudad)

#acceder a un solo atributo o clave del diccionario
nombre=persona ["nombre"]
print(nombre)

print(persona["nombre"])

persona['nombre']='Arnoldo Iguaran'
print(persona['nombre'])
print(persona)

persona["saldoEnCuenta"]= 0
print(persona['saldoEnCuenta'])
print(persona)

#Recorriendo un diccionario
for valor in persona.values():
    print(valor)