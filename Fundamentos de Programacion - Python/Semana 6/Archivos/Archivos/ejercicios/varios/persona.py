import json
"""LISTA DE DICCIONARIOS"""

ls=[]

for i in range(3):
    dicc={}
    dicc["nombre"]="a"+str(i)
    dicc["edad"]="edad-"+str(i)
    ls.append(dicc)

print(ls)

with open("personas.json", "w") as fl:
    json.dump(ls,fl,indent=4)

with open("personas.json", "r") as fl:
    datos=json.load(fl)

print(datos)


ls2=[[1,2],[3,4],[5,6]]

with open("lista.json", "w") as fl:
    json.dump(ls,fl,indent=4)

with open("lista.json", "r") as fl:
    datos2=json.load(fl)

print(type(datos2))
print(datos2[0])
print(type(datos2[0]))