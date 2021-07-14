"""OPERACIONES BASICAS CON CADENAS DE CARACTERES O STRING"""

"""Concatenar (unir) cadenaS"""
# cad1="hola"
# cad2="a"
# cad3="todos"
#
# cad4=cad1+cad2+cad3
# print(cad4)
# cad4=cad1+" "+cad2+" "+cad3
# print(cad4)


"""Obtener la longitud o cantidad de caracteres de una cadena"""
# NOTA: los espacios en blanco también cuentan como un caracter
# Observa la diferencia entre las 2 cadenas
# print(len(cad4))
# cad4=cad4+" "
# print(len(cad4))

"""Recorrerr una cadena y obtener sus caracteres"""
# c="bienvenidos"
#
# for i in c:
#     print(i) #i, toma el valor de cada caracter
#
# #acceder a un caracter de la cadena.
# #Observe que una cadena es un conjunto de caracteres, se pueden acceder por un indice
# print("\n",c[3])
#
# #otra forma de reccorrer
# for i in range(0,len(c)):
#     print(c[i])

##Obtener el último
# print(c[-1])
# print(c[len(c)-1])
#
# ##obtener el penúltimo
# print(c[-2])
# print(c[len(c)-2])

##todo: EJERCICIO hacer un ciclo que muestre los caracteres en orden inverso, desde el último al primero##
# for i in range(,,):
#     print(c[])


"""Obtener Subcadenas """
c="bienvenidos"
print(c[0:2])  #obtiene los caracteres desde 0 a 2 (2 no lo incluye)
# print(c[0:5])
print(c[0:len(c)])  #obtiene todos, de 0 hasta la ultima posicion
print(c[4:len(c)])  #empieza desde el indice 4
# print(c[0:]) #desde 0 hasta la ultima
# print(c[:5]) #desde 0 hasta la posicion 4.
print(c[:]) #que resultado produce?


"""comparar cadenas"""
# todo: notar la diferencia entre las 2 comparaciones
# cad1="hola"
# cad2="Hola"
# # print(cad1==cad2)
#
# cad1="hola"
# cad2="hola"
# print(cad1==cad2)

# todo: observar el comportamiento de la comparacion
# cad1="0"
#
# print(cad1==0) #resultado False
# print(cad1=="0") #resultado True


###todo: TIP-RETO
"""dividir cadenas"""
"""el metodo cadena.split() retorna una lista con las palabras separadas"""

# cad1="hola como estan todos"
# cad1 = "   hola     como están   todos    "
# cad2 = "hola-como-están-todos"
# cad3="hola-como.estan/todos;es,un-gusto saludarlos"
# cad4="hola - como - estan - todos"

# print(cad1.split()) #elimina todos los espacios en blanco, inicio, final, en medio, solo deja las palabras
# print(cad2.split("-")) #separa por el simbolo "/", pero los espacios en blanco permanecen
# print(re.split("[\,\.\;\-\/\ ]",cad3)) #para dividir por varios simbolos es necesario: import re
# print(f"esta({cad4.split('-')}") ##todo: SUPER-TIP-RETO

###todo: TIP-RETO
"""Eliminar espacios en blanco"""

###eliminar espacios en blanco al inicio y final con strip()
# cad1="  hola como estan  "
# cad2="      -  hola como estan todos -       "

# print(f"({cad1})")
# print(f"({cad1.strip()})")
# print(f"esta({cad2.strip(' - ')})")

###todo: SUPER-TIP-RETO. Eliminar caracter final
# cad1 = "   hola   /como  /estan  /  todos/"
# cad2 = cad1[0:-1] #1-forma. Crear subcadena desde 0 a penultimo caracter
# cad3=cad1.strip("/") #2-forma. Quitar caracter final con '/'
cad4="- hola a todos /     "
# print(cad1)
# print(cad2)
# print(cad3)
# print(f"({cad4.lstrip(' -')})")
# print(f"({cad4.rstrip(' /')})")

print()
###eliminar espacios en blanco entre palabras y eliminar caracter final '/'
# cad1 = "   hola   /como     /estan    /  todos/"
# print(cad1.split("/"))
#
# cad2 = cad1.strip(("/"))
# n = cad2.split("/")
# print(n)
#
# for i in range(0, len(n)):
#     n[i] = n[i].strip()
#
# print(n)
#
# cad3="hola -como -estan -todos"
# print(cad3.split(maxsplit=1)) #envio la max-cantidad de divisiones
# print(cad3.split("-",maxsplit=2)) #con caracter separador




