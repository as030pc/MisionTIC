"""------------------------------CONJUNTO DE SUBPROGRAMAS----------------------------------------"""
#<editor-fold desc="SUBPROGRAMAS">


#<editor-fold desc="mostrarLetras()">
"""mostrar las  letras que hay en una cadena usando ciclo For"""
def mostrarLetras(cadenaparamostrar):
    n=len(cadenaparamostrar)

    for i in range(0,n):
        print(cadenaparamostrar[i])

#</editor-fold>

#<editor-fold desc="contarLetras(cad1,letra)">
""" cuentas las letras que hay en cadenaparacontar. 
letraparacontar, es la letra que se contara en cadenaparacontar"""
def contarLetras(cadenaparacontar, letraparacontar):
    n=len(cadenaparacontar)
    contadorletras=0

    for i in range(0,n):
        if(cadenaparacontar[i]==letraparacontar):
            contadorletras+=1

    return contadorletras
#</editor-fold>

#<editor-fold desc="contarVocales(cadena)">
"""contar cuantas veces aparece una vocal en una cadena"""
def contarVocales(cadena):
    a=contarLetras(cadena,"a")
    e=contarLetras(cadena,"e")
    i=contarLetras(cadena,"i")
    o=contarLetras(cadena,"o")
    u=contarLetras(cadena,"u")

    return f"total:\n a-{a} e-{e} \n i-{i} o-{o} \n u-{u}"

#</editor-fold>

#<editor-fold desc="implementar contarVocales2(cadena)">
##todo: Completar el código del subprograma
"""cuenta las vocales en una cadena"""
def contarVocales2(cadena):

    for i in cadena:
        if(i=="a"):
            pass
        elif (i=="e"):
            pass
        elif (i=="i"):
            pass
        elif(i=="o"):
            pass
        elif(i=="u"):
            pass

    # return f"total:\n a-{cona} e-{cone} \n i-{coni} o-{cono} \n u-{conu}"

#</editor-fold>

#<editor-fold desc="cadenaMasLongitud(cad1,cad2)">
def cadenaMasLongitud(cad1,cad2):
    c1=len(cad1)
    c2=len(cad2)

    if(c1==c2):
        return f" ({cad1}) y ({cad2}) son iguales en longitud"
    else:
        if(c1>c2):
            return f"({cad1}) tiene más longitud que ({cad2})"
        else:
            return f"({cad2}) tiene más longitud que ({cad1})"

#</editor-fold>

#<editor-fold desc="contarPalabras(palabras)">
def contarPalabras(palabras):
    lista_palabras=palabras.split("-")
    cantidad_palabras=len(lista_palabras)

    return cantidad_palabras
#</editor-fold>

#</editor-fold>

"""---------------------PROGRAMA PRINCIPAL--------------------------------------"""

#<editor-fold desc="PROGRAMA PRINCIPAL">

#<editor-fold desc="ejecucion mostrarLetras(cad1)">
##todo EJECUCIÓN DE mostrarLetras(cad)##
#cad="bienvenidos"
# mostrarLetras(cad)

#</editor-fold>

#<editor-fold desc="ejecucion contarLetras(cad1,letra)">
# ###todo EJECUCIÓN DE contarLetras(cad, l) ##
# cad="bienbeb"
# letra="b"
# x=contarLetras(cad,letra)
# print(f" Hay {x},{letra}, en {cad}")

#</editor-fold>


#<editor-fold desc="ejecucion contarVocales(cad1)">
###ejecucion de contar vocales
# cad="aeioaei"
# print(contarVocales(cad))
# print(contarVocales2()) #todo: desarrollar subprograma

#</editor-fold>

#<editor-fold desc="ejecucion de cadenaMasLongitud(cad1,cad2">
###ejecucion de cadenaMasLongitud
# cad1="saludo"
# cad2="saludo"
# print(cadenaMasLongitud(cad1,cad2))

#</editor-fold>

#<editor-fold desc="ejecucion de contarPalabras(pal)">
###todo ejecución de contarPalabras()
pal="hola-a-como-estan-el"
print("palabras:",contarPalabras(pal))

#</editor-fold>

#</editor-fold>


"""------------------------------CONJUNTO DE SUBPROGRAMAS----------------------------------------"""
#<editor-fold desc="SUBPROGRAMAS">
"""suma 2 cadenas digito a digito. Las 2 cadenas deben ser iguales"""
#<editor-fold desc="sumarCadenas()">
def sumarCadenas(cad1, cad2):
    resultado = ""
    for i in range(0, len(cad1)):
        suma = int(cad1[i]) + int(cad2[i])  # sumo digito a digito de las 2 cadenas
        resultado += str(suma) + "-"  # concateno en resultado la suma digito de las 2 cadenas

    return resultado

#</editor-fold>

#<editor-fold desc="sumarCadenaenLista()">
"""suma los valores de una lista. ls['1','2','3'] resultado es 6"""
def sumarCadenaenLista(ls):
    suma=0
    for i in range(0,len(ls)):
        suma=suma+int(ls[i])

    return suma
#</editor-fold>

#<editor-fold desc="sumarCadenaSuper">
"""suma una cadena que tiene el formato 1-2 @ 3-4 cuyo resultado es: 3 - 7"""
def sumarCadenaSuper(cad1):
    # primero divido la cadena en subcadenas delimitadas por "/". [12-24-38, 34-25-200]
    primera_division = cad1.split("@")
    print(primera_division)

    resultado=""
    #segundo,divido cada elemento de la primera división y lo separo por "-"
    for i in range(0,len(primera_division)):
        suma=sumarCadenaenLista(primera_division[i].split("-"))
        resultado=resultado+str(suma) + " : "


    # print()
    # print(primera_division)
    # print(primera_division[0].split("-"))
    # print(primera_division[1].split("-"))
    return resultado.strip(" :")

#</editor-fold>

#</editor-fold>
"""---------------------PROGRAMA PRINCIPAL--------------------------------------"""
#<editor-fold desc="PROGRAMA PRINCIPAL">

#<editor-fold desc="Ejecución de sumarCadenas()">
##todo: ejecucion de sumarCadenas() - se suma digito a digito
# cad1="123"
# cad2="456"
# # resultado esperado es: 5 7 9
# print(sumarCadenas(cad1,cad2))

#</editor-fold>

#<editor-fold desc="Ejecución de sumarCadenaenLista()">
##todo: ejecucion de sumarCadenaenLista(). Se suman los elementos que estan dentro de la lista
# cad1=["1","20","3","5","1","-15"]
# print(sumarCadenaenLista(cad1))

#</editor-fold>

#<editor-fold desc="Ejecución de sumarCadenaSuper()">
##todo: ejecucion de sumarCadenaSuper(). Se suman los elementos de la cadena separados por "-" y por "@"
# cad1 = "1-2 @ 3-4"
# ##resultado esperado: 3 : 7
# print(sumarCadenaSuper(cad1))

#</editor-fold>

#<editor-fold desc="implementar">
##todo: implementar multiplicarCadenaSuper(cad1)
# cad1="1 : 2 : 3 : 4 = 1 : 2 : 2"
##resultado esperado: 24 # 4

##todo: implementar restarCadenaSuper(cad1)
# cad1="4 = 2 = 1 # 2 = 4"
##resultado esperado: 2 _ -2
#</editor-fold>

#</editor-fold>