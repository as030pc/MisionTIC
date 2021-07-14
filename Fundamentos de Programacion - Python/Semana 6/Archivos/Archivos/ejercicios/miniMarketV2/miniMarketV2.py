import json

def iniciarInventario():
    productos={"manzanas":0,
           "peras":0,
           "mangos":0
           }

    with open("minimarket.json", "w") as fl:
        json.dump(productos,fl,indent=4)

def verInventario():
    with open("minimarket.json", "r") as fl:
        datos=json.load(fl)
    print()
    print(datos)
    print()


"""agrega un producto al archivo"""
def agregarInventarioalArchivo(producto,cantidad):

    ###leo el archivo
    with open("minimarket.json", "r") as fl:
        datos = json.load(fl)

    clave=datos.get(producto) #busco en el diccionario y aumento la cantidad
    if(clave!=None): #si encontró el producto en el diccioario entra.
        datos[producto]+=cantidad

    ###escribo en el archivo
    with open("minimarket.json", "w") as fl:
        json.dump(datos,fl,indent=4)

    ###todo: ejercicio para clase.
    with open("minimarket.json", "r") as fl:
        datos=json.load(fl)
    print("Inventario actualizado: ",datos)


"""quitar productos al inventario al vender"""
def quitarInventarioalArchivo(producto,cantidad):
    with open("minimarket.json", "r") as fl: ##leo datos
        datos=json.load(fl)

    verificarproducto=datos.get(producto)
    if (verificarproducto!=None):
        datos[producto]-=cantidad


    with open("minimarket.json", "w") as fl: ##escribo los nuevos datos
        json.dump(datos,fl)

    with open("minimarket.json", "r") as fl:
        datos=json.load(fl)

    print("inventario actualizado: ",datos)



"""---------------EJECUCION--------------------"""
# iniciarInventario()
# agregarInventarioalArchivo("mangos",3)



while True:

    print("-----MINI SUPERMARKET----")
    print("0. Ver Inventario")
    print("1. Comprar manzanas")
    print("2. Comprar peras")
    print("3. Comprar mangos")
    print("4. iniciar Inventario en 0")
    print("-----------VENTAS----------")
    print("5. Vender manzanas")
    print("6. Vender peras")
    print("7. Vender mangos")
    print("Salir - presione cualquier tecla")

    opc=input("digite opcion:")

    if(opc=="0"):
        verInventario()
    elif(opc=="1"):
        agregarInventarioalArchivo("manzanas",int(input("digite cantidad de manzanas: ")))
    elif (opc=="2"):
        agregarInventarioalArchivo("peras", int(input("digite cantidad de peras: ")))
    elif (opc=="3"):
        agregarInventarioalArchivo("mangos", int(input("digite cantidad de mangos: ")))
    elif (opc=="4"):
        iniciarInventario()
    elif (opc=="5"):
        quitarInventarioalArchivo("manzanas",int(input("cantidad de manzanas a vender: ")))
    ###todo: implementar las otras ventas
    else:
        break

