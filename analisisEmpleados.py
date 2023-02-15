import pandas as pd
import matplotlib.pyplot as plt

empleados=pd.read_csv("./empleados.csv")


analistasBajocosto=empleados[(empleados["salario"]<=5000000) & (empleados["cargo"]=="analista1")].head(20)

#exportar un data frame hacia html

archivoHTML= analistasBajocosto.to_html()
archivoGenerado=open("bajoCosto.html","w")
archivoGenerado.write(archivoHTML)
archivoGenerado.close()
