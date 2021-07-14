import json

def crearArchivoVacio():
    with open("acumulador.json","w") as fl:
        json.dump({"acumulador":0},fl)
        print("Archivo creado")

def aumentarAcumulador(n):
    with open("acumulador.json","r") as fl:
        datos=json.load(fl)

    print(datos)
    datos["acumulador"]+=n

    print(datos)

    with open("acumulador.json","w") as fl:
        json.dump(datos,fl)
        print("archivo actualizado")

def verArchivo():
    with open("acumulador.json","r") as fl:
        datos=json.load(fl)

    print(datos)

"""------------EJECUCIÓN------------"""

# crearArchivoVacio()

