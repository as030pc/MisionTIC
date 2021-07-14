"""TRADUCTOR V1.  traduce WE ARE FAST a NOSOTROS SOMOS VELOZ(ES) de forma manual"""

dicc={
        "SHE":"ELLA",
        "HE":"EL",
        "WE":"NOSOTROS" ,
        "IS":"ES",
        "ARE":"SOMOS",
        "INTELLIGENT":"INTELIGENTE(S)",
        "FRIENDLY":"AMIGABLE(S)",
        "FAST":"VELOZ(ES)",
        "STRONG":"FUERTE"
    }

"""Traducir conjunto de palabras"""

##lo basico
# print(dicc["STRONG"])


##dividir la cadena por espacios en blanco

cad="WE ARE FAST"
lista=cad.split() #lista con las palabras separadas
print(lista)


###muestro datos individualmente
pal1=dicc[lista[0]]
pal2=dicc[lista[1]]
pal3=dicc[lista[2]]

# print(pal1,pal2,pal3)
rdo=""
# rdo=pal1+pal2+pal3 #los valores estan unidos
# rdo=pal1+" "+pal2+" "+pal3
# print(rdo)


###ahora con for
for i in range(0,len(lista)):
    # print(lista[i]) #muestra las claves
    print(dicc[lista[i]]) #muestra los valores
    rdo=rdo+dicc[lista[i]]+" "  #concatenando las traducciones

# rdo=rdo.strip()  ##eliminando espacios en blanco
print(f"({rdo})")

###con otro for
# for i in lista: ##en i, se almacena las claves
#     rdo=rdo+dicc[i]+" "
#
# print(rdo.strip)


##todo: Ejercicio.
##implementar un dicionario que almacene numeros y nombres de jugadores
## y realice la siguiente traduccion
##11 10 9 1 8  a CUADRADO JAMES FALCAO OSPINA CARDONA
##las claves deben ser cadenas o string. Ej "10"

equipo_futbol = {'11': 'Cuadrado', '10': 'James', '9': 'Falcao', '1': 'Ospina', '8': 'Cardona'}


for i in equipo_futbol:
    print(f'La camisa del jugador {equipo_futbol[i]} es {i}', end= '; ')




"""DICCIONARIO CON SUBPROGRAMAS"""
import random
"""Se implementa un traductor de ingles a español. Entrada: SHE IS FAST Salida: ELA ES VELOZ(ES) con subprogramas"""

"""SUBPROGRAMAS"""
#region SUBPROGRAMAS

#region EnEs()
"""Traduce una palabra de inges a español"""
"""palabra_en_inges es la palabra de ingles a traducir"""
def EnEs(palabra_en_ingles): #THEY
    dicc={ "SHE":"ELLA",
           "HE":"EL",
             "WE":"NOSOTROS" ,
             "IS":"ES",
             "ARE":"SOMOS",
             "INTELLIGENT":"INTELIGENTE(S)",
             "FRIENDLY":"AMIGABLE(S)",
              "FAST":"VELOZ(ES)",
                "STRONG":"FUERTE"
          }

    return str(dicc.get(palabra_en_ingles))

#endregion

#region traductorSuper1()
"""traduce una cadena a español. Ej: SHE IS FAST = ELLA ES VELOZ(ES)"""
def traductorSuper1(cadena_palabras):
    #divido la cadena por sus espacios
    palabras=cadena_palabras.split()
    resultado=""

    for i in palabras:
        # print(EnEs(i))
        resultado=resultado+EnEs(i)+" "

    return resultado

#endregion

#region traductorSuper2()

###todo: implementar el siguiente subprograma
"""traduce una cadena a ingles. Ej: ELLA ES VELOZ(ES) = SHE IS FAST"""

def traductorSuper2(cadena_palabras):
    pass


#endregion

#endregion










"""TRADUCTOR V3. traduce SHE-IS-FAST @ WE-ARE-STRONG a ELLA ES VELOZ(ES) NOSOTROS SOMOS FUERTES """

def EnEs(palabra_en_ingles): #THEY
    dicc={ "SHE":"ELLA",
           "HE":"EL",
             "WE":"NOSOTROS" ,
             "IS":"ES",
             "ARE":"SOMOS",
             "INTELLIGENT":"INTELIGENTE(S)",
             "FRIENDLY":"AMIGABLE(S)",
              "FAST":"VELOZ(ES)",
                "STRONG":"FUERTE"
          }

    return str(dicc.get(palabra_en_ingles))

def traductorSuper1(cadena_palabras):
    #divido la cadena por sus espacios
    palabras=cadena_palabras.split(" @ ")
    rdo=""

    for i in palabras:
        lpal=i.split("-")
        for k in lpal:
            rdo=rdo+EnEs(k)+" "

    return rdo


"""IMPLEMENTAR ESTA FUNCION"""
def traductorSuper2(cadena_palabras):
    rdo = ""



    return rdo


"""-------------------EJECUCION--------------------------"""

dicc = {"SHE": "ELLA",
        "HE": "EL",
        "WE": "NOSOTROS",
        "IS": "ES",
        "ARE": "SOMOS",
        "INTELLIGENT": "INTELIGENTE(S)",
        "FRIENDLY": "AMIGABLE(S)",
        "FAST": "VELOZ(ES)",
        "STRONG": "FUERTE(S)"
        }

cad="SHE-IS-FAST @ WE-ARE-STRONG" #Salida: ELLA ES VELOZ(ES) NOSOTROS SOMOS FUERTES


##PRIMERO DE FORMA MANUAL

lista1=cad.split(" @ ")  #divido la cadena en oraciones, delimitadas por, @
# print(lista1)

lpal1=lista1[0].split("-") #separo la cadena SHE-IS-FAST en [SHE, IS, FAST]. pal1 es una lista con las claves de lista1[0]
# print("lista-pal1 ",lpal1)
lpal2=lista1[1].split("-") #pal2, es una lista con las claves de lista1[1]
# print("lista-pal2 ",lpal2)



# print(lpal1[0])
rdo1=""
rdo1=dicc[lpal1[0]] + dicc[lpal1[1]] + dicc[lpal1[2]]
# print(rdo1)

# print(lpal2[2])
rdo2=""

rdo2=dicc[lpal2[0]] + dicc[lpal2[1]] + dicc[lpal2[2]]
# print(rdo2)

rdofinal=rdo1+" "+rdo2

# print(rdofinal)

###AHORA CON FOR

lista1=cad.split(" @ ")
# print(lista1)

rdofinal=""

for i in lista1:
    # print(i)
    lpal=i.split("-")
    # print(lpal)
    for k in lpal:
        # print(k)
        rdofinal+=dicc[k]+" "

# print(rdofinal)


###CON EL OTRO FOR
# rdofinal2=""
# for i in range(len(lista1)):
#     print(lista1[i])
#     lpal=lista1[i].split("-")
#     for k in range(len(lpal)):
#         rdofinal2+=dicc[lpal[k]]+" "
#
#
# print(rdofinal2)


"""--------------------------------------------------------"""
"""AHORA CON FUNCIONES"""

cad="SHE-IS-STRONG @ WE-ARE-INTELLIGENT"
print(traductorSuper1(cad))


#region
cad2="ELLA/ES/FUERTE/ = NOSOTROS/SOMOS/INTELIGENTE(S)/"
#endregion

##todo: implementar funcion traductorSuper2() para que reciba:

cad1="SHE,IS,STRONG - WE,ARE,INTELLIGENT"
#formato de salida: ELLA/ES/FUERTE/ = NOSOTROS/SOMOS/INTELIGENTE(S)/


###NO MODIFICAR
# if(cad2==traductorSuper2(cad1)):##cad2 ya tiene un valor asignado
#     # print("EL EJERCICIO ESTA BIEN HECHO. FELICITACIONES!!!")
# else:
#     print("PARECE QUE ALGO ESTA MAL, REVISA TU CÓDIGO")








""""--------------------EJECUCIÓN DE PROGRAMA PRINCIPAL--------------------------"""
#region EJECUCION DE PROGRAMA PRINCIPAL

#region Ejecucion de EnEs()
##todo: ejecución de la función: EnEs() para traducir palabras###

# x=EnEs("IS")
# print(x)

#endregion

"""ejecucion de traductorSuper()"""
#region Ejecucion de traductorSuper()
##todo: ejecucion de la funcion: traductorSuper1()

frase_ingles="SHE IS FRIENDLY HE IS FAST"
rdo=traductorSuper1(frase_ingles)
print(rdo)

#endregion


#region Ejecucion de traducir digitando por teclado
"""traduce la palabra en ingles digitada"""
# palabra=input("digitar palabra a traducir: ")
# print(f" {palabra}, significa: {dicc[palabra]} ")

#endregion


#region Ejecucion de mostrar con datos aleatorios(para analizar)
"""buscar con datos aleatorios :"""
##todo: muchachos para que lo analizen##
# print(dicc.keys())
# lista_claves=list(dicc.keys()) #convierto las claves a Lista
# clave=random.randint(0,len(lista_claves)-1)
# print(clave)
# print(lista_claves[clave])
# print(f"{lista_claves[clave]} = {dicc.get(lista_claves[clave])}")

#endregion

#endregion

##todo: ejercicio:
###crear un diccionario y funciones que traduzcan
#10/1 # 11/9 a JAMES-OSPINA @ CUADRADO-FALCAO poner mas jugadores





