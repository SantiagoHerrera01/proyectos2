import pandas as pd
#Cargar datos para poder analizar
#1. declarar variable donde almacenar la fuente de datos
fuenteDatos=pd.read_csv("./empleados.csv")
print(type(fuenteDatos))
#Obtener N cantidad de datos (Filtro)
#ver primeros registros
filtrohead=fuenteDatos.head()
print (filtrohead)
print("\n")
#ver una cantidad de registros en el inicio
filtrohead2=fuenteDatos.head(15)
print ("\n")
print(filtrohead2)
print("\n")
#ver ultimos 5 registros
filtrotail=fuenteDatos.tail()
print (filtrotail)
print("\n")
#ver ultimos registros dependiendo el numero seleccionado
filtrotail2=fuenteDatos.tail(30)
print(filtrotail2)
print("\n")


#acceder a un solo atributo o clave del diccionario

filtroNombre=fuenteDatos.head(10)["nombres"]
print(filtroNombre)
print("\n")

#Filtros por filas

filtroIloc=fuenteDatos.iloc[[5,15]]
print(filtroIloc)
print("\n")


#1. mostrar primeros 50 empleados
filtro50=fuenteDatos.head(50)
print(filtro50)
print("\n")
#2. de los pirmeros 50 empleados mostrar solo salario
filtrosalario=fuenteDatos.head(50)["salario"]
print(filtrosalario)
print("\n")
#3. obtener informacion general de los 500 registros encontando la media aritmetica de los salarios
filtroMedia=fuenteDatos.describe()
print(filtroMedia)
print("\n")

#4. obtener datos registro 100,200,300,400
filtroEmp=fuenteDatos.iloc[[100,200,300,400]]
print(filtroEmp)
print("\n")
#5. obtener ulimos 3 empleados solo ver nombre y salario
filtroult3=fuenteDatos.tail(3)[["nombres","salario"]]
print(filtroult3)
print("\n")