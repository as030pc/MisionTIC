import csv

"""leer csv"""

archivo=open("estudiantes.csv", "r")
datos=csv.DictReader(archivo,delimiter=",")

# print(datos.fieldnames) #muestra el encabezado


"""mostra el nombre de la persona que tiene el mayor promedio"""
"""mostra el nombre de la persona que tiene el menor promedio"""
prom_general=[]
nombre_mayor=""
mayor=-1
nombre_menor=""
menor=10


for i in datos:
    # print(i)
    prom = (float(i["n1"]) + float(i["n2"])) / 2
    prom_general.append(prom)

    if (prom > mayor):
        mayor = prom
        nombre_mayor = i["nombre"]

    if (prom < menor):
        menor = prom
        nombre_menor = i["nombre"]

print(f"El mayor promedio lo tiene: {nombre_mayor}, con: {mayor}")
print(f"El menor promedio lo tiene: {nombre_menor}, con: {menor}")

promg=sum(prom_general)/len(prom_general) #con sum se suman todos los datos de la lista
print(f"Promedio general: {promg}")


"""Mostrar datos - solo para verificar lo de arriba """
archivo=open("estudiantes.csv", "r")
datos=csv.DictReader(archivo,delimiter=",")
lista_estudiantes=[]
fila=[]

for i in datos:

    fila.append(i["nombre"])

    prom = (float(i["n1"]) + float(i["n2"])) / 2

    fila.append(i["n1"])
    fila.append(i["n2"])
    fila.append(prom)

    if (prom > mayor):
        mayor = prom
        nombre_mayor = i["nombre"]

    if (prom < menor):
        menor = prom
        nombre_menor = i["nombre"]

    lista_estudiantes.append(fila)
    fila=[]

print()
print("------Estudiantes---------")
for i in lista_estudiantes:
    print(i)

