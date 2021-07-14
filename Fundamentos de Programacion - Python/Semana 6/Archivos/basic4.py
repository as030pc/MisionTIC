import json

"""crear json con listas de listas"""


ls=[[1,2],[3,4],[4,5]]

"""escribir archivo json"""
with open("test4.json", "w") as fl:
    json.dump(ls, fl,indent=4)


"""leer un json"""
with open("test4.json", "r") as fl:
    ls=json.load(fl) ##convierte el json a un diccionario

print(ls)
print(type(ls))

for i in range(0,len(ls)):
    print(ls[i])

ls.append([6,7])
print(ls)
ls[0].append(10)
ls[1].append(10)
ls[2].append(10)
ls[3].append(10)
print(ls)

print()
for i in range(0,len(ls)):
   for k in range(0,len(ls[0])):
       print(ls[i][k],end=" ")
   print()



