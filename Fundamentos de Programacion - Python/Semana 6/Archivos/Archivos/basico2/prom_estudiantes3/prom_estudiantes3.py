import json
"""Agrega notas y estudiantes en lista de listas"""


def crearArchivoVacio():
    datos={"totalestudiantes":0, "listane":[]}

    with open("promedio3.json","w") as fl:
        json.dump(datos,fl)
        # print("Archivo creado")

def agregar(est,nota):
    with open("promedio3.json","r") as fl:
        datos=json.load(fl)

    print(datos)
    datos["totalestudiantes"]+= 1
    datos["listane"].append([est,float(nota)])

    print(datos)

    with open("promedio3.json","w") as fl:
        json.dump(datos,fl)
        # print("archivo actualizado")

def verArchivo():
    with open("promedio3.json","r") as fl:
        datos=json.load(fl)

    print(datos)

def verconPromedio():
    with open("promedio3.json", "r") as fl:
        datos = json.load(fl)

    # print(datos)
    print(datos["listane"])
    # prom=sum(datos["listanotas"])
    # print(datos)

    sum=0
    for i in range(0,len(datos["listane"])):
        sum+=datos["listane"][i][1]

    print(sum/len(datos["listane"]))


    # prom=sum(datos["listanotas"])/len(datos["listanotas"])
    # return prom



"""------------EJECUCIÓN------------"""

# crearArchivoVacio()
agregar("c",4)
# verArchivo()
verconPromedio()




