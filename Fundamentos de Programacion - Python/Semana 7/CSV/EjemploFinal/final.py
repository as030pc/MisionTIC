import csv

##lee un archivo enviando el nombre del archivo
def leerArchivo(archivo):
    archivo = open(archivo, "r")
    datos = csv.DictReader(archivo) #datos es un diccionario y se recorre con for

    return datos

##Escribe un archio. Recibe el nombre del archivo, los datos para escribir y el encabezado
def escribirArchivo(nombre_archivo, datos, encabezado):
    print(datos)
    print(encabezado)

    with open(nombre_archivo, "w", newline="", encoding="utf-8") as fl:
        escritor = csv.writer(fl, delimiter="\t")
        escritor.writerow(encabezado)
        escritor.writerows(datos)


##-------------EJECUCION---------------------

"""----------calcular el mayor y menor de los promedios-----------"""
lspro=[] #guarda la lista de todos los promedios de los datos del archivo
lista_datos=leerArchivo("datos.csv")

print()
for i in lista_datos:
    print(i)
    prom=(float(i["n1"])+float(i["n2"]))/2
    lspro.append(prom)

# print(lspro)
print("el mayor de los promedios es : ",max(lspro))
print("el menor de los promedios es : ",min(lspro))
promedio_total=sum(lspro)/len(lspro)
print("El promedio general de todos los datos es: ",promedio_total)

# escribirArchivo1("rdo2",drdo,"nombre\tn1\tn2\tpromedio\tconcepto\n")


"""--------calcular quien tiene el mayor promedio con nombre-----------"""
lspro=[]
lista_datos=leerArchivo("datos.csv")
nombre=""
mayor=-1
nombre_menor=""
menor=10


print("mayor")
for i in lista_datos:
    # print(i)
    prom=(float(i["n1"])+float(i["n2"]))/2

    if(prom>mayor):
        mayor=prom
        nombre=i["nombre"]

    if(prom<menor):
        menor=prom
        nombre_menor=i["nombre"]

print(nombre,mayor)
print(nombre_menor,menor)



"""------Escribir estado aprobó o se rajo------"""
archivo=leerArchivo("datos.csv")
linea=[]  #almacena cada línea del archivo para ser escrito
lista_datos=[] #almaceno la lista de datos

for i in archivo: #recorro la lista de diccionarios

    linea.append(i["nombre"])
    linea.append(i["n1"])
    linea.append(i["n2"])

    prom = (float(i["n1"]) + float(i["n2"])) / 2
    linea.append(prom)

    if(prom>=3):
        linea.append("Pasó")
    else:
        linea.append("Se rajó")

    lista_datos.append(linea)
    linea=[]

print("archivo")
escribirArchivo("rdo.csv", lista_datos, ["nombre", "n1", "n2", "promedio", "concepto"])










