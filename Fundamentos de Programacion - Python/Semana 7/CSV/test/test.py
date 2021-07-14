import csv

# Leer el archivo 'estudiantes.csv' con reader() y
# mostrar todos los registros, uno a uno:

# with open('estudiantes.csv') as csvarchivo:
#     entrada = csv.reader(csvarchivo)
#     for reg in entrada:
#         print(reg)

archivo=open(r'../basico/datosbasicos1.csv', "a+")
# print(archivo.read())
# print(archivo.readlines()) #devuelbe una lista

archivo.write("linea4\n")
archivo.seek(0)
for i in archivo.readlines():
    print(i)

        # lista.append(reg)

# print(lista)





# datos = csv.reader(open('estudiantes.csv'))
# reg=next(datos)
# print(reg)
# # print(type(datos))
#
# for i in datos:
#     print(i)



