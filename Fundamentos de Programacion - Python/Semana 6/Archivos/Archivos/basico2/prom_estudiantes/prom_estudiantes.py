import json

def crearArchivoVacio():
    datos={"totalestudiantes":0, "listanotas":[]}

    with open("promedio.json","w") as fl:
        json.dump(datos,fl)
        # print("Archivo creado")

def agregarNota(nota):
    with open("promedio.json","r") as fl:
        datos=json.load(fl)

    print(datos)
    datos["totalestudiantes"]+= 1
    datos["listanotas"].append(float(nota))

    print(datos)

    with open("promedio.json","w") as fl:
        json.dump(datos,fl)
        # print("archivo actualizado")

def verArchivo():
    with open("promedio.json","r") as fl:
        datos=json.load(fl)

    print(datos)

def verconPromedio():
    with open("promedio.json", "r") as fl:
        datos = json.load(fl)

    print(datos["listanotas"])
    # prom=sum(datos["listanotas"])

    prom=sum(datos["listanotas"])/len(datos["listanotas"])
    return prom



"""------------EJECUCIÓN------------"""

# crearArchivoVacio()
# agregarNota(2)
# verArchivo()
# print(verconPromedio())




