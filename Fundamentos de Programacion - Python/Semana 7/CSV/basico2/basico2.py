import csv

"""leer csv"""

archivo=open("estudiantes.csv", "r")
datos=csv.DictReader(archivo,delimiter=",")

# print(datos.fieldnames) #muestra el encabezado

print()
lrdo=[]
fila=[] #nombre,n1,n2,promedio,aprobo/se rajo

for i in datos:
    print(i)
    # print(i["nombre"],end=" ")

    fila.append(i["nombre"]) #agrego nombre del diccionario a la fila
    fila.append(i["n1"])    #agrego n1(nota1) del diccionario a la fila
    fila.append(i["n2"])    #agrego n2(nota2) del diccionario a la fila
    prom=(int(i["n1"])+int(i["n2"]))/2 #calculo el promedio de n1 y n2
    fila.append(prom)  #agrego prom a la fila

    if(prom>=3):
        fila.append("aprobó") #agrego aprobó a la fila
    else:
        fila.append("se rajó") #agrego se rajó a la fila

    lrdo.append(fila)
    fila=[]   #Se debe inicializar la fila en cero

print()
print(lrdo)

"""----------------------------------------------------------"""
"""escribir csv, con los nuevos datos"""
#encabezado( nombre,n1,n2,promedio,aprobo/se rajo)
encabezado=["nombre","n1","n2","promedio","estado"] #representa la primera fila del archivo


#abro el archivo para escribir datos
with open("estudiantes2.csv", "w", newline="", encoding="utf-8") as archivo:
    escritor=csv.writer(archivo, delimiter="\t")
    escritor.writerow(encabezado)
    escritor.writerows(lrdo)




"""Leó el archivo recién creado (estudiantes2)"""
# file2=open("estudiantes2.csv",encoding="utf-8")
# data=csv.DictReader(file2,delimiter='\t')
#
# for i in data:
#     print(i)


