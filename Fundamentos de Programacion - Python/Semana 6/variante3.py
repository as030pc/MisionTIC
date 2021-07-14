#NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, sirven para probar tu código en consola, y el funcionamiento de la clase cliente
#from pruebas import pruebas_codigo_estudiante
#from cliente import cliente
"""NOTAS: 
    -PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    -LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO
"""


"""Inicio espacio para programar funciones propias"""
#En este espacio podrás programar las funciones que deseas usar en la función solución (ES OPCIONAL

#NO MODIFICAR, NI AGREGAR CÓDIGO EN ESTE ARCHIVO
class cliente:
  def __init__(self, nombre, edad, dinero_cuenta_bancaria, fila_interes, transaccion, cantidad_retirar, cantidad_consignar):
    self.nombre = nombre
    self.edad = edad
    self.dinero_cuenta_bancaria = dinero_cuenta_bancaria
    self.fila_interes = fila_interes
    self.transaccion = transaccion
    self.cantidad_retirar = cantidad_retirar
    self.cantidad_consignar = cantidad_consignar

"""Fin espacio para programar funciones propias"""

def sede_bancaria(cola_general):
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.

    cola_caja = []
    cola_info = []
    suma_retiros = 0
    suma_consignaciones = 0
    edad_minima_retiro = -1
    edad_minima_consignacion = -1
    edad_minima_info = -1

    for i in cola_general:
        cliente = i
        if cliente.fila_interes == "caja":
            cola_caja.append(cliente.nombre)
            if cliente.transaccion == "retirar":
                if edad_minima_retiro == -1:
                    edad_minima_retiro = cliente.edad
                elif cliente.edad <= edad_minima_retiro:
                    edad_minima_retiro = cliente.edad
                suma_retiros = suma_retiros + cliente.cantidad_retirar

            elif cliente.transaccion == "consignar":
                if edad_minima_consignacion == -1:
                    edad_minima_consignacion = cliente.edad
                elif cliente.edad <= edad_minima_consignacion:
                    edad_minima_consignacion = cliente.edad
                suma_consignaciones = suma_consignaciones + cliente.cantidad_consignar


        else:
            cola_info.append(cliente.nombre)
            if edad_minima_info == -1:
                edad_minima_info = cliente.edad
            elif cliente.edad <= edad_minima_info:
                edad_minima_info = cliente.edad








    
    return cola_caja, cola_info, suma_retiros, suma_consignaciones, edad_minima_retiro, edad_minima_info, edad_minima_consignacion

"""
NO PEDIR DATOS CON LA FUNCIÓN input(), NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED CREE
Esta línea de código que sigue, permite probar si su ejercicio es correcto
Por favor NO ELIMINARLA, NO MODIFICARLA
"""

#pruebas_codigo_estudiante(sede_bancaria)

cola_general = [cliente("Matt",21,235000,"caja","retirar",100000,0), cliente("Dan",32,658000,"caja","retirar",98000,0), cliente("Diana",29,87000,"info","ninguna",0,0)]

sede_bancaria(cola_general)

print(sede_bancaria(cola_general))