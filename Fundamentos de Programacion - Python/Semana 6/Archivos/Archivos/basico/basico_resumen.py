import json

###todo: para trabajar con archivos json, usamos Diccionarios

"""basico"""

###1 ejemplo con un solo dato en un diccionario
t1={"dato":1}

with open("test1.json","w") as fl: #se crea el archivo con nombre: test1.json en el directorio actual con permiso de escritura "w"
    json.dump(t1,fl)

###2 ejemplo - con varios datos en el diccionario

t2={"dato1":10,"dato2":20,"dato3":3.1,"dato4":4.5}

with open("test1.json","w") as fl:
    json.dump(t2,fl)

###3 ejemplo - usando una lista


t3={"lista":[1,2,3,4]} #con 1 lista
with open("test1.json","w") as fl:
    json.dump(t3,fl)

t3 = {"lista1": [1, 2, 3, 4], "lista2":[5,6,7,8],"lista3":[9,10,11]} #con varias listas
with open("test1.json", "w") as fl:
    json.dump(t3, fl)

t3={"listasuper":[[1,2],[3,4],[5,6]]} #se guarda como matriz
with open("test1.json","w") as fl:
    json.dump(t3,fl)



###4 ejemplo - usando tuplas
#en json una tupla se representa como lista

t4={"tupla1":(1,2,3),"tupla2":(4,5,6)}

with open("test1.json","w") as fl:
    json.dump(t4,fl)


###ejemplo con parametro indent, con tuplas
t4={"tupla1":(1,2,3),"tupla2":(4,5,6)}
# t4={"a":1,"b":2,"c":3}

with open("test1.json","w") as fl:
    json.dump(t4,fl,indent=4)


### ejemplo - serializo un diccionario como json y lo almaceno en un string js

# t={"a":1,"b":2,"c":3}
# js=json.dumps(t) #uso dumps (s de string) requiere un solo parametro. Serviria para transmitir por red
#
# print(type(js))
# print(js)



"""usando diccionarios anidados"""
# d1={"a":1,"b":2,"c":3}
# d2={"d":4,"e":5}
#
# dd={"dicc1":d1,"dicc2":d2,"dato":None,"dato2":3.5}
# with open("test1.json","w") as fl:
#     json.dump(dd,fl)

"""usando varios diccionarios"""
# t4={"a":{"dato1":1,"dato2":2}, "b":{"dato3":3,"dato4":4}}
#
# with open("test1.json","w") as fl:
#     json.dump(t4,fl,indent=4)

"""usando listas de listas"""
# t4={"l1":[[1,2],[3,4]],
#     "l2":[[5,6],[7,8]]
#     }
#
# with open("test1.json","w") as fl:
#     json.dump(t4,fl,indent=4)

"""usando diccionarios y listas"""

t4={"equipo":"superHero",
    "ciudad":"NewYork",
    "active":True,
    "members":
    [
        {"nombre":"batman", "edad":30,"poderes":["Volar","subir edificios"]},
        {"nombre":"superman", "edad":40,"poderes":["vision laser","super fuerza"]},
        {"nombre":"aquaman", "edad":25,"poderes":["nadar","super velocidad"]},
        {"nombre":"tor", "edad":28,"poderes":["superfuerza","martillo magico"]},

    ]

    }

with open("test1.json","w") as fl:
    json.dump(t4,fl, indent=4)


"""-----usando objetos--------"""
class Persona:

    def __init__(self, nom,ed):
        self.nombre=nom
        self.edad=ed


per1=Persona("Andrea",20)
per2=Persona("Catalina",35)
per3=Persona("Esperanza",28)

t4={
    "persona1": {"nombre":per1.nombre, "edad":per1.edad},
"persona2": {"nombre":per2.nombre, "edad":per2.edad}

}
with open("test1.json","w") as fl:
    json.dump(t4,fl,indent=4)


"""----------------RECUPERANDO ARCHIVOS JSON-------------------"""
"""Se accede al archivo y se carga sus datos con el método load() - devuelbe un diccionario"""

t1={"a":1,"b":2, "c":[1,2,3,4]}
with open("test1.json","w") as fl:
    json.dump(t1,fl, indent=4)

###cargo los datos del archivo con load()
with open("test1.json","r") as fl:
    datos=json.load(fl) #datos es de tipo diccionario



"""serializo y deserializo la cadena de str"""
t1={"a":1,"b":2, "c":[1,2,3,4]}
js=json.dumps(t1) #js es un str con formato json
d=json.loads(js) #d es un diccionario, que fue cargado de un json str

print(js)
print(type(js))
print(d)
print(type(d))

"""  """
datos={"a":1,"b":2}

print(datos.get("c","no encontrado"))






