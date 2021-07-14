import json

"""Archivo con contador """

def crearArchivoVacio():
    with open("contador.json","w") as fl:
        json.dump({"contador":0},fl)
        print("Archivo creado")

def aumentarContador():
    with open("contador.json","r") as fl:
        datos=json.load(fl)

    print(datos)
    datos["contador"]+=1

    print(datos)

    with open("contador.json","w") as fl:
        json.dump(datos,fl)
        print("archivo actualizado")

def verArchivo():
    with open("contador.json","r") as fl:
        datos=json.load(fl)

    print(datos)

"""------------EJECUCIÓN------------"""

# crearArchivoVacio()
aumentarContador()
verArchivo()






