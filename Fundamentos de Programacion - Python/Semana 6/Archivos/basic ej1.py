import json
"""CREAR Y LEER JSON"""

"""crear diccionario"""

dicc={"nombre":"paola", "edad":20}

"""escribir archivo json"""
with open("test.json", "w") as fl:   #w: escribirlo, fl es un alias
    json.dump(dicc, fl,indent=4)     #indent: da una estructura de identacion


"""leer un json"""
with open("test.json", "r") as fl:
    dicc=json.load(fl) ##convierte el json a un diccionario

print(dicc)
print(type(dicc))

print(dicc["nombre"])