import json

"""crear json con listas"""

ls=[1,2,3]
ls2=[[1,2],[3,4],[4,5]]

"""escribir archivo json"""
with open("test3.json", "w") as fl:
    json.dump(ls2, fl,indent=4)


"""leer un json"""
with open("test3.json", "r") as fl:
    ls=json.load(fl) ##convierte el json a un diccionario

print(ls)
print(type(ls))

for i in range(0,len(ls)):
    print(ls[i])

ls.append([4,5])
print(ls)
# ls.append(5)
# print()
# for i in range(0,len(ls)):
#     print(ls[i])