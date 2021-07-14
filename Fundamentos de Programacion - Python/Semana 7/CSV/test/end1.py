import csv

#leer csv
datos=[]

with open('estudiantes.csv') as csvarchivo:
    entrada = csv.reader(csvarchivo)
    for reg in entrada:
        print(reg)
        datos.append(reg)

datos.pop(0)
print(datos)



# ESCRIBIR EN UN NUEVO ARCHIVO NOMBRE, PROMEDIO
archivo2=open(r'prom.csv', "a")
lspaso=[]
lsquedo=[]

print()
for i in datos:
    print(i)

    pr=(int(i[3])+int(i[4]))/2
    if(pr>=3):
        rdo="paso"
        lspaso.append(pr)
    else:
        rdo="se rajo"
        lsquedo.append(pr)

    archivo2.write(f"{i[0]}\t{pr}\t{rdo}\n")

print(f"pasaron: {len(lspaso)} y su max promedio es: {max(lspaso)} minimo es: {min(lspaso)}")
print(f"quedaron: {len(lsquedo)} y su max promedio es: {max(lsquedo)} minimo es: {min(lsquedo)}")
