import csv

"""leer csv"""

archivo=open("datosbasicos1.csv", "r")
datos=csv.DictReader(archivo,delimiter=",") #datos guarda la información del archivo como un diccionario

print(datos.fieldnames) #muestra el encabezado

print()
for i in datos:
    print(i)
    # print(i["nombre"],end=" ")
    # print(i["edad"],end=" ")
    # print(i["ciudad"],end=" ")
    # print(i["n1"],end=" ")
    # print(i["n2"])

a="saludo"
print("hola a todos"+a)


"""escribir csv"""
encabezado=["nombre","edad"] #representa la primera fila del archivo
datosw=[["paola",25],["leonidas",30]] #datos a llenar en el archivo csv


#abro el archivo para escribir datos
with open("datosbasicos12.csv","w",newline="") as archivo:
    escritor=csv.writer(archivo, delimiter="\t") #separador en tabulaciones
    escritor.writerow(encabezado) #Encabezado
    escritor.writerows(datosw) #contiene lista de listas

"""Leer con delimitacor tab (\t)"""
# archivo2=open("datosbasico2.csv","r")
# datos2=csv.DictReader(archivo2,delimiter="\t")
# print(datos2.fieldnames)
#
# for i in datos2:
#     print(i)


