from vector import vector
# from metodos import *
import random
import math
# import metodos as m
from metodos import *


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

    n=10

    vobj=vector(n)
    vobj.V[0]=n

    vpar=vector(n)
    vimpar=vector(n)


    # for i in range(1,n+1):
    #     vobj.V[i]=random.randint(1,20)
    construyeVector(vobj,n,1,20)

    vcopia=vector(n)
    vcopia.V=vobj.V.copy()

    print(vcopia.V)
    conp=1
    for i in range(1,n+1):
        if(vcopia.V[i]%2==0):
            vpar.V[conp]=vcopia.V[i]
            vpar.V[0] = conp
            conp=conp+1



    print(vpar.V)
    seleccion(vpar)
    imprimeVector(vpar)
    print(vpar.V)


    # print(vobj.V)
    # print(vcopia.V)
    #
    # seleccion(vcopia)
    # print(vcopia.V)




    #sumar datos del vector
    # print(vobj.V)
    # # sm=sumarDatos(vobj)
    # print("promedio: ",sumarDatos(vobj)/n)



    #buscar datos
    # print(vobj.V)
    # ib=buscarDato(vobj,10)
    # print("dato: ",ib)

    #intercambiar
    # print(vobj.V)
    # intercambiar(vobj,1,n)
    # print(vobj.V)


    #menor
    # print(vobj.V)
    # nm=menor(vobj)
    # print("numero menor es: ",vobj.V[nm])
    # print("indice numero menor es: ", nm)


#obtener indice del mayor
    # print(vobj.V)
    # nm=mayor(vobj)
    # print("numero mayor es: ",vobj.V[nm])
    # print("indice numero mayor es: ", nm)




#par 0, impar 1
    # print(vobj.V)
    # for i in range(1,n+1):
    #     if(vobj.V[i]%2==0):
    #         vobj.V[i]=0
    #     else:
    #         vobj.V[i]=1
    #
    # print(vobj.V)


    #contar numero de veces
    # print(vobj.V)
    # num=int(input("numero: "))
    # con=0
    #
    # for i in range(1,n+1):
    #     if(vobj.V[i]==num):
    #         con=con+1
    #
    # print(vobj.V)
    # print(f"{num} esta: {con} veces")



#intercambiar
    # print(vobj.V)
    # aux=vobj.V[1]
    # vobj.V[1]=vobj.V[n]
    # vobj.V[n]=aux
    #
    # print(vobj.V)



    # for i in range(1,n+1):
    #     print(vobj.V[i])





    #elevar al cuadrado
    # print(vobj.V)
    # for i in range(1,n+1):
    #     vobj.V[i]=vobj.V[i]**2
    # print(vobj.V)






    #mostrar al revez
    # for i in range(n,0,-1):
    #     print(vobj.V[i])




    # vobj.V[0] = n
    # construyeVector(vobj, n, 1, 10)
    # print(vobj.V)

solucion()



