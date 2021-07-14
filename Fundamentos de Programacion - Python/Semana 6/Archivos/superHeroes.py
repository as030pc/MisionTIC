import json
"""ESCRIBIR EN ARCHIVO Y RECUPERAR LOS DATOS CON SUPERHEROES"""
"""Este ejercicio muestra diferentes niveles de acceso"""
"""Se crear un archivo json con el diccionario t4 y luego se carga y se muestra sus datos 1 po 1"""

t4={
"equipo1":
     {
        "nombre":"superHero",
        "ciudad":"NewYork",
        "active":True,
        "miembros":
            [
                {"nombre":"batman", "edad":30,"poderes":["Volar","subir edificios"]},
                {"nombre":"superman", "edad":40,"poderes":["vision laser","super fuerza"]},
                {"nombre":"aquaman", "edad":25,"poderes":["nadar","super velocidad"]},
                {"nombre":"tor", "edad":28,"poderes":["superfuerza","martillo magico"]},

            ],
     },

"equipo2":{
    "nombre":"superFire",
    "ciudad":"Miami",
    "active":False,
    "miembros2":
        [
            {"nombre":"mujer maravilla", "edad":38,"poderes":["latigo","artes marciales"]},
            {"nombre":"Hulk", "edad":50,"poderes":["super fuerza"]},
            {"nombre":"antman", "edad":25,"poderes":["velocidad","super pequeño"]},
            {"nombre":"spiderman", "edad":24,"poderes":["telaraña","trepar edificios"]},

        ]

},

    ###todo: agregar equipo 3

    }

###crear archivo
with open("superheroes.json", "w") as fl:
    json.dump(t4,fl, indent=4)

###Leer archivo
with open("superheroes.json", "r") as fl:
    datos=json.load(fl) #datos es de tipo diccionario

print(datos)

# print( datos.keys())
"""Acceder a datos"""
### ver claves - equipos
# for i in datos:
#     print(i)



"""ver descripcion de equipos"""

##Equipo 1
print()
print("descirpción de equipo1")
print(datos["equipo1"])
print(datos["equipo1"]["nombre"])
print(datos["equipo1"]["ciudad"])
print(datos["equipo1"]["active"])
print(datos["equipo1"]["miembros"])

print()
print("miembros de equipo1")
print(datos["equipo1"]["miembros"][0]) #batman
print(datos["equipo1"]["miembros"][1]) #superman
print(datos["equipo1"]["miembros"][2]) #aquaman
print(datos["equipo1"]["miembros"][3]) #tor

print()
print("datos personales de miembros")
print()
##batman
print(datos["equipo1"]["miembros"][0]["nombre"])
print(datos["equipo1"]["miembros"][0]["edad"])
print(datos["equipo1"]["miembros"][0]["poderes"])
print(datos["equipo1"]["miembros"][0]["poderes"][0])
print(datos["equipo1"]["miembros"][0]["poderes"][1])

print()
##superman
print(datos["equipo1"]["miembros"][1]["nombre"])
print(datos["equipo1"]["miembros"][1]["edad"])
print(datos["equipo1"]["miembros"][1]["poderes"])
print(datos["equipo1"]["miembros"][1]["poderes"][0])
print(datos["equipo1"]["miembros"][1]["poderes"][1])

print()
##aquaman
print(datos["equipo1"]["miembros"][2]["nombre"])
print(datos["equipo1"]["miembros"][2]["edad"])
print(datos["equipo1"]["miembros"][2]["poderes"])
print(datos["equipo1"]["miembros"][2]["poderes"][0])
print(datos["equipo1"]["miembros"][2]["poderes"][1])

print()
##tor
print(datos["equipo1"]["miembros"][3]["nombre"])
print(datos["equipo1"]["miembros"][3]["edad"])
print(datos["equipo1"]["miembros"][3]["poderes"])
print(datos["equipo1"]["miembros"][3]["poderes"][0])
print(datos["equipo1"]["miembros"][3]["poderes"][1])


###todo: Implementar: mostrar los datos del equipo2, como el codigo de arriba

""##Equipos 2
