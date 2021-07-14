from vector import vector
# from metodos import *
import random
import math

def construyeVector(vec, m, r1, r2):
    vec.V[0] = m
    for i in range(1, m + 1):
        vec.V[i] = random.randint(r1, r2)

def imprimeVector(vec, mensaje="vec-n: \t"):
        print("\n", mensaje,"\n", end="")
        for i in range(1, vec.V[0]+1):
            print(vec.V[i], end=", ")
            if i % 30 == 0:
                print("\n", end ="")

def solucion():
    # n = random.randint(1, 10)
    n=5

    vobj=vector(n)
    vobj.V[0]= n #La posicion 0 se llena con el numero de elementos
    vobj.V[1]=70
    print(vobj.V[1])
    print(vobj.V[2])
    print(vobj.V)

    # vobj.V[0] = n
    # construyeVector(vobj, n, 1, 10)
    # print(vobj.V)

solucion()



