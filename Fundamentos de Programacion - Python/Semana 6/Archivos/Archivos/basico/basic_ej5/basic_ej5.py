"""json con diccionarios con listas y demás combinaciones"""
import json

dicc1=[[1,2],[3,4],[5,6]]

dicc2={
        "codigo1": [1,2,3],
        "codigo2":[4,5,6],
        "codigo3":[7,8,9]
}

dicc3= {
        "codigo1": {"nombre":"Paola", "edad":30},
        "codigo2":{"nombre":"Andres","edad":45},
        "codigo3":{"nombre":"Catalina","edad":30}
}

dicc4=[
        {"codigo":"100","nombre":"paola","edad":30},
        {"codigo":"200","nombre":"Andres","edad":20},
        {"codigo":"300","nombre":"Catalina","edad":40},
    ]

dicc5=[
        {"codigo":"100","nombre":"paola","notas":[2,3,4]},
        {"codigo":"200","nombre":"Andres","notas":[3,4,2]},
        {"codigo":"300","nombre":"Catalina","notas":[4,5,2]},
    ]

with open("test.json", "w") as fl:
    json.dump(dicc1,fl,indent=4)



