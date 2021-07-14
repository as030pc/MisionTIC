import json

def crearArchivoVacio():
    datos={"totalsuma":0,"totalnumeros":0}

    with open("sumar2.json","w") as fl:
        json.dump(datos,fl)
        # print("Archivo creado")

def sumar2(n1,n2):
    with open("sumar2.json","r") as fl:
        datos=json.load(fl)

    print(datos)
    datos["totalsuma"]+=n1+n2
    datos["totalnumeros"]+=2

    print(datos)

    with open("sumar2.json","w") as fl:
        json.dump(datos,fl)
        # print("archivo actualizado")

def verArchivo():
    with open("sumar2.json","r") as fl:
        datos=json.load(fl)

    print(datos)

"""------------EJECUCIÓN------------"""

# crearArchivoVacio()
sumar2(3,4)
verArchivo()
