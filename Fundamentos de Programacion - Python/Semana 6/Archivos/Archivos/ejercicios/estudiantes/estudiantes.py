import json


"""crear el archivo con 1 estudiante"""
def crearArchivo():
    # e1 = Estudiante("100", "e1", 2, 3, 4)
    # e2=Estudiante("b","200",3.5,3,2.9)

    # dicc = {e1.getCodigo():
    #             {"nombre": e1.getNombre(),
    #              "notas": [e1.getN1(), e1.getN2(), e1.getN3()]
    #              }
    #         }

    dicc = {}

    with open("estudiantes.json", "w") as fl:
        json.dump(dicc,fl,indent=4)


def listadoEstudiantes():
    with open("estudiantes.json", "r") as fl:
        datos=json.load(fl)

    for i in datos:
        print(f"{i} {datos[i]['nombre']} {datos[i]['notas']}")
    # print("Listado: ", datos)


"""agregar estudiante al archivo"""
def agregarEstudiante(cod,nom,n1,n2,n3):
    with open("estudiantes.json", "r") as fl:
        datos=json.load(fl)
    # print(datos)
    # buscarClave=datos.get(cod)
    # if(buscarClave!=None):
    datos[cod]={"nombre":nom,"notas":[n1,n2,n3]}
    # print(datos)
    #
    with open("estudiantes.json", "w") as fl:
        json.dump(datos,fl,indent=4)

    listadoEstudiantes()

def verNotasEstudiante(cod):
    with open("estudiantes.json", "r") as fl:
        datos=json.load(fl) #leo el archivo y lo guardo en el diccionario, datos


    estudiante=datos.get(cod) #busco el codigo en el diccionario
    if(estudiante!=None): #si el estudiante existe entra
        print(f"{estudiante['notas']}, promedio: {sum(estudiante['notas'])/len(estudiante['notas'])}")

def promedioGeneral():
    with open("estudiantes.json", "r") as fl:
        datos = json.load(fl)  # leo el archivo y lo guardo en el diccionario, datos
    # print(type(datos))
    rdo=0
    for i in datos:
        # print(i)
        print(datos[i]["notas"])
        print(sum(datos[i]["notas"])/len(datos[i]["notas"]))
        rdo+=sum(datos[i]["notas"])/len(datos[i]["notas"])

    print(len(datos))
    print(rdo)
    print("promedio general: ",rdo/len(datos))

"""----------------EJECUCIÓN-------------------"""

# crearArchivo()
# with open("estudiantes.json","r") as fl:
#     datos=json.load(fl)
# print(datos)

# listadoEstudiantes()
# verNotasEstudiante("100")


while(True):
    print("-------------MENÚ------------")
    print("0. Crear Archivo")
    print("1. Ver listado de estudiantes")
    print("2. Agregar estudiante ")
    print("3. Ver notas de Estudiante")
    print("4. Ver promedio general")
    print(" Salir")

    opc=input("opcion: ")
    if opc=="0":
        crearArchivo()
    elif opc=="1":
        listadoEstudiantes()
    elif opc=="2":
        agregarEstudiante(input("codigo: "), input("nombre: "),float(input("N1: ")),float(input("N2: ")),float(input("N3: ")))
    elif opc=="3":
        verNotasEstudiante(input("codigo: "))
    elif opc == "4":
        promedioGeneral()
    else:
        break



