"""Crear diccionario"""

# dicc={} #diccionario vacio
dicc={"she":"ella",
      "he":"el",
      "we":"nosotros",
      "they":"ellos"

      }   #diccionario con clave y valor


"""Acceder a elementos del diccionario. Se hace por su clave"""
# print(dicc["she"]) #accediendo a un elemento del diccionario con clave "she". Distingue Mayusculas y minusculas
# print(dicc.get("she"))
# print(dicc)


"""Asignando valores"""
# dicc["he"]="el" #agrego otro elemento clave-valor
#
# dicc["we"]="osotros"  #creo otra clave-valor
#
# dicc["we"]="nosotros" #modifico una clave-valor
#
# n=dicc["we"]  #asignando a n, el contenido de una clave-valor
# print(dicc)
# # print(n)

#
# #Analizar la siguiente instrucción. Las claves son únicas y distingue Mayúsculas y minúsculas. they != They
# dicc["they"]="ellos"
# dicc["They"]="ellos con otra clave"


"""Recorrer diccionarios"""
#mostrar solo claves
# for i in dicc:
#       print(i)

#mostrar solo los valores. Se usa get(clave)
#se recomienda usar get(clave)  ya que si no encuentra el valor devuelbe None.
# for i in dicc:
#       print(dicc.get(i))

#mostrar clave y valor
# for i in dicc:
#     print(f"Clave:{i} - Valor: {dicc.get(i)}")

#otra forma de mostra clave y valor
# for i,k in dicc.items():
#       print(i,k)


"""Eliminar una clave - valor"""

# print(dicc)
# dicc.pop("They")
# del dicc["They"]
#
# print(dicc)


""""aumentar valor"""

# dicc["cantidad"]=1
# # print(dicc["cantidad"])
# dicc["cantidad"]+=10
# print(dicc["cantidad"])

"""------OTROS MÉTODOS----------------"""

"""obtengo la longitud del diccionario o cantidad de elementos"""
# ld=len(dicc)
# # print("El total de palabras es: ", ld)
# print(dicc)


"""obtengo todas las claves"""
# print(dicc.keys())

# ls=dicc.keys()
# for i in ls:
#      print(i)

# print(type(ls))


"""obtengo todos los valores"""
# print(dicc.values())
# lv=dicc.values()
#
# for i in lv:
#     print(i)

"""obtengo claves y valores"""
# print(dicc.items())
#
# lit=dicc.items()
# for i in lit:
#     print(i)


"""fusionando diccionarios"""
# d1={"a":1, "b":1}
# d2={"b":8,"c":3}
# d1.update(d2)
# print(d1)
# print(d2)

"""copiando diccionarios"""
# d1={"a":10}
# d2=d1.copy()
#
# print(d2)


"""comprobar si existe una clave"""
#si no encuentra la clave devuelbe None
# d1={"a":0,"b":1}
# if(d1.get("a")!=None):
#     print("Existe")
# else:
#     print("No existe")


# d1={"a":0,"b":1}

"""Dicionarios anidados"""
# d1={"a":1,"b":2}
# d2={"c":2,"d":3}
#
# d3={"anidado1":d1,
#     "anidado2":d2
#     }
#
# print(d3)
# # print(d3["anidado1"])
# # print(d3["anidado1"]["a"])
#
# for i in d3:
#       # print(i,d3[i])
#       for k in d3[i]:
#             print(k,d3[i][k],sep="-")
#       print()

"""convertir 2 listas en un diccionario"""
ls1=["producto","cantidad"]
ls2=["manzanas",8]
dicc=dict(zip(ls1,ls2))
print(dicc)
print(type(dicc))








