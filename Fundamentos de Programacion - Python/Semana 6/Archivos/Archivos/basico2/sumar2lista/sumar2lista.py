import json

def crearArchivoVacio():
    datos={"totalsuma":0,"totalnumeros":0,"listanumeros":[]}

    with open("sumar2lista.json","w") as fl:
        json.dump(datos,fl)
        # print("Archivo creado")

def sumar2(n1,n2):
    with open("sumar2lista.json","r") as fl:
        datos=json.load(fl)

    print(datos)
    datos["totalsuma"]+=n1+n2
    datos["totalnumeros"]+=2
    datos["listanumeros"].append([n1,n2])

    print(datos)

    with open("sumar2lista.json","w") as fl:
        json.dump(datos,fl)
        # print("archivo actualizado")

def verArchivo():
    with open("sumar2lista.json","r") as fl:
        datos=json.load(fl)

    print(datos)

"""------------EJECUCIÓN------------"""

# crearArchivoVacio()
sumar2(1,3)
verArchivo()
