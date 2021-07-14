import json

"""crear json con multiples diccionarios"""

dicc={ "100": {"nombre":"Paola", "edad":20},
        "200": {"nombre":"Leonardo","edad":35}
        ###todo: crear mas personas
    }

"""escribir archivo json"""
with open("test.json", "w") as fl:
    json.dump(dicc, fl,indent=4)


"""leer un json"""
with open("test.json", "r") as fl:
    dicc=json.load(fl) ##convierte el json a un diccionario

print(dicc)
print(type(dicc))

print(dicc["200"])
print(dicc["200"]["edad"])
# print(dicc["100"]["edad"])

##mostrar con for
# for i in dicc:
#     print(i) ##en i, tengo la clave del diccionario
#     print(dicc[i]["nombre"], end="-") ##acedo a los subdiccinarios
#     print(dicc[i]["edad"])

