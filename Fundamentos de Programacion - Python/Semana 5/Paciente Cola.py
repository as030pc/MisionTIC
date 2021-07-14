from Cola import Cola
"""clase Padre"""
class Persona:

    def __init__(self, nom,ced): #Constructor de la clase padre
        self.nombre=nom
        self.cedula=ced


"""Clase Paciente - hereda de Persona"""
class Paciente(Persona):

    def __init__(self,nom, cedu, ciudad,eps): #Constructor de la clase hija
        super().__init__(nom,cedu) #Super accede a las metodos de la clase padre
        self.ciudad=ciudad
        self.eps=eps

    def obtenerCiudad(self):
        return self.ciudad

    def obtenerEps(self):
        return self.eps

    def __str__(self):
        return f"{self.nombre, self.cedula, self.ciudad, self.eps}"

"""PROGRAMA PRINCIPAL"""

"""Prueba manual"""

est=Paciente("a", "10", "ipiales", "eps1")
est1=Paciente("b", "11", "medellin", "eps2")
est2=Paciente("c", "12", "bogota", "eps3")

c1=Cola()
c1.agregar(est)
c1.agregar(est1)
c1.agregar(est2)
# c1.quitar()
# print(c1.inicioCola())
# print(c1.inicioCola().obtenerCiudad())
# print(c1.tamano())
# print(c1.items)

"""con Menu y ciclo While"""
c=Cola()
opc=1

"""Completar lo que debe realizar las  opciones del Menú"""

while (opc!=0):
    print("--------MENÚ---------- ")
    print("1- Agregar Paciente a la cola")
    print("2- Ver primer Paciente de la cola ")
    print("3- Atender Paciente")
    print("4- Ver cantidad de Pacientes")
    print("5- Ver si hay pacientes para atender")
    print(" - para salir digite cualquier otro número ")
    print()

    opc=int(input("Digite opción: "))

    if(opc==1):
        #pass #esta debe borrarse, solo era para parar el while

        #tip1: leer los 4 datos que tiene el objeto
        nombre = input(f'Ingrese el nombre del paciente:')
        cedula = input(f'Ingrese la cedula del paciente:')
        ciudad = input(f'Ingrese el nombre del paciente:')
        eps = input('Ingrese la eps:')

        pac = Paciente(nombre, cedula, ciudad, eps)
        c.agregar(pac)

        #tip2: crear un objeto de tipo Paciente()

        #tip3: agregar el paciente a la cola



    elif (opc==2):
        #pass
        #formato de salida
        m = c.inicioCola()
        print('El primer paciente es el Señor(a):', m)
        # ('a', '10', 'ipiales', 'eps1')
        print()
    elif (opc==3):
        #pass #esta debe borrarse
        print('Se atendio al paciente', c.quitar())
        #tip: quitar el elemento de la Cola
    elif (opc==4):
        #pass
        #formato de salida
        print(f'Hay, {c.tamano()} pacientes en cola')
        #Hay 2, pacientes en la cola
        print()
    elif (opc==5):
        #pass
        if c.estaVacia():
            print('No hay pacientes para atender')
        else:
            print('No hay pacientes por atender')

            #Formato de salida
            #Si hay Pacientes para atender
            #No hay Pacientes para atender

    else:
        print("Gracias por usar nuestro servicio.....")
        break


