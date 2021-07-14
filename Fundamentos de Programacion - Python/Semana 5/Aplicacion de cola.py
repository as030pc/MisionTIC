from Cola import Cola
"""juego de la papa caliente"""
def TintoTango(listaNombres, N): #N es el conteo del juego
    colaSimulacion = Cola()
    for nombre in listaNombres:  #Va por cada elemento del argumento ingresado en la funcion
        colaSimulacion.agregar(nombre)

    while colaSimulacion.tamano() > 1:
        for i in range(N):
            colaSimulacion.agregar(colaSimulacion.quitar()) #El primero de la cola lo mando atras

        colaSimulacion.quitar()

    return colaSimulacion.quitar()


'Programa principal'
print(TintoTango(["Hector", "David", "Susana", "Juan"], 3))