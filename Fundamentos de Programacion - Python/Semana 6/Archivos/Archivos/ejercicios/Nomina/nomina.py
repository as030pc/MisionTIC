import json



def nominaVacia():
    with open("nomina.json","w") as fl:
        json.dump([],fl,indent=4)
        print("Nomina en 0")

def agregarEmpleado(emp):
    try:
        with open("nomina.json","r") as fl:
            datos=json.load(fl)

    except IOError as e:
        print("no se pudo abrir el archivo",e)

    datos.append([10, 10, 10])

    with open("nomina.json","a") as fl:
        json.dump(datos,fl)

# def guardarNomina():
#
#         with open("nomina.json","w") as fl:
#             json.dump(listaEmpleados,fl)





# nominaVacia()
agregarEmpleado([5,2,3])
# agregarEmpleado([4,2,3])
# print(listaEmpleados)
# guardarNomina()

