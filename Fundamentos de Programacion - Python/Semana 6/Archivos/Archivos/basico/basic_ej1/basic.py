import json
"""CREAR Y LEER JSON"""

"""crear diccionario"""

dicc={"nombre":"paola", "edad":20,"ciudad":"cali"}


"""escribir archivo json"""
with open("test.json", "w") as fl:
    json.dump(dicc, fl,indent=4)




"""leer un json"""
with open("test.json", "r") as fl:
    dicc=json.load(fl) ##convierte el json a un diccionario

print(dicc)
print(dicc["ciudad"])
dicc["sueldo"]=200

print(type(dicc))
#
# print(dicc["nombre"])