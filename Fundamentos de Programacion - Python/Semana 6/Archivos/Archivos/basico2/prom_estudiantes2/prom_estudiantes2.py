import json

def crearArchivoVacio():
    datos={"totalestudiantes":0,"listaestudiantes":[], "listanotas":[]}

    with open("promedio2.json","w") as fl:
        json.dump(datos,fl,indent=4)
        # print("Archivo creado")

def agregarNota(est,nota):
    with open("promedio2.json","r") as fl:
        datos=json.load(fl)

    print(datos)
    datos["totalestudiantes"]+= 1
    datos["listaestudiantes"].append(est)
    datos["listanotas"].append(float(nota))

    print(datos)

    with open("promedio2.json","w") as fl:
        json.dump(datos,fl,indent=4)
        # print("archivo actualizado")

def verArchivo():
    with open("promedio2.json","r") as fl:
        datos=json.load(fl)

    print(datos)

def verconPromedio():
    with open("promedio2.json", "r") as fl:
        datos = json.load(fl)

    print(datos["listanotas"])
    # prom=sum(datos["listanotas"])

    prom=sum(datos["listanotas"])/len(datos["listanotas"])

    for i,k in zip(datos["listaestudiantes"], datos["listanotas"]):
        print(f"estudiante: {i}, nota: {k}")

    print("Promedio: ",prom)




"""------------EJECUCIÓN------------"""

# crearArchivoVacio()
agregarNota("d",5)
# verArchivo()
verconPromedio()




