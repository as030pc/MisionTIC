

# SUBPROGRAMAS
import random
from metodos import *


def mensaje(b):
    r = b+b
    return r

a = 10
n = mensaje(a)
print(n)



# Subprograma que sume dos numeros

def sumar(a,b):
    r = a+b
    return r


suma = sumar(4,5)
print(suma)


# Ejemplos

def cubo(a):
    cubo = a**3

    return cubo

a=cubo(3)

print(a)


# ------------------------

def incremento(cantidad):
    cantidadnueva = cantidad*1.1

    return cantidadnueva

precio =incremento(3)

print(precio)

#---------------------------

def promedio(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3)/3

    return promedio

promedio1 =promedio(3,3,3)

print(promedio1)

#----------------------------
def numero(number):
    if (number<=0):
        return False

    else:
        return True


condicion1 = numero(-9)

print(condicion1)


#----------------------------


# Numero primo

def esPrimo(n):
    con = 0
    for i in range(2,n):
        if (n%i ==0):
            con = con+1

    if(con>=1):
        return False
    else:
        return True


n = esPrimo(7)

if (n == False):
    print('El numero no es primo')
else:
    print('El numero no es primo')




## VECTORES

vec = [8, 12, 19,23]
print(vec[0]) #Imprimir un vector
vec[1] = 55   # Asignar un elemento nuevo al vector

vec[1]+=10
print(vec[1])
print(vec)

for i in range(0, 4):
  print(vec[i])


# Encontrar el mayor
#vec = [8, 12, 19,23]
#mayor = 0
#for i in range(0,4):
    #if(vec[i]>vec[mayor]):
        #mayor= i
#print('el indice es', mayor)
#print('El mayor es ', vec[mayor])

#Intercambiar

#aux = vec[0]
#vec[0] = vec [5]
#vec[5] = aux
#print(vec)


#Determinar si es par o impar
for i in range(0,4):
    if(vec[i]%2 ==0):
        vec[i] = 0
    else:
        vec[i] = 1
print(vec)

# Serie de Fibonacci

vec= [0,1,1,2,0,0,0]
vec[0] = 0
for i in range(0,7):
    vec[i] = vec[i]+vec[i-1]

print(vec)



### PROGRAMACION ORIENTADA A OBJETOS

from vector import vector


def solucion():
    n = 5

    vobj = vector(n)
    vobj.V[0] = n  # La posicion 0 se llena con el numero de elementos
    vobj.V[1] = 70
    print(vobj.V[1])
    vobj.V[2] = 80
    vobj.V[3] = 90
    vobj.V[4] = 34
    vobj.V[5] = 4

    print(vobj.V)

    for i in range(1, n+1):

        vobj.V[i] = random.randint(1,20)#Imprime desde la posicion cero
    print(vobj.V)
   #Mostrar al reves
    #for i in range(n,0, -1):
        #print(vobj.V[i])

    #Elevar los elementos al cuadrado
    #for i in range(1, n+1):

        #vobj.V[i] = vobj.V[i]**2
    #print(vobj.V)

    #Sacar raiz cuadrada
    #for i in range(1, n+1):
        #vobj.V[i] = vobj.V[i]**(1/2)
    #print(vobj.V)

    #Intercambiar
    aux = vobj.V[1]
    vobj.V[1] = vobj.V[n]
    vobj.V[n] = aux
    print(vobj.V)

    #par 0, impar 1
    print(vobj.V)
    for i in range(1, n + 1):
        if (vobj.V[i] % 2 == 0):
            vobj.V[i] = 0
        else:
            vobj.V[i] = 1
    print(vobj.V)


## PROGRAMA METODOS
    # Seleccion: Ordena el vector de manera ascendente
    for i in range(1, n+1):
        vobj.V[i] = random.randint(1,20)
    print(vobj.V)
    burbuja(vobj) #Ordenar de manara ascendente
    print(vobj.V)
    seleccion(vobj) #Ordenaar de manera descendente
    nn = mayor(vobj)
    sm = sumarDatos(vobj)
    print(sm)




# #Crear una copia
#
#     #construyeVector(vobj, n, 1, 20)
#     vcopia = vector(n)
#     vcopia.V = vobj.V.copy()
#
#     print(vobj.V)
#     print(vcopia.V)

solucion()

