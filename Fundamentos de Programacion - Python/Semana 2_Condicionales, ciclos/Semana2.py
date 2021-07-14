""""
# Uso de elif
opc = 2
if (opc ==0):
  print('La opcion es ' ,opc)
elif (opc == 1):
  print('La opcion es' ,opc)
else:
  print('Ningna')




#Ciclo while


#imprimir del 50 al 80
con =50

while(con<=80):
  print(con)
  con = con + 1

#pedir tres notas y calcular el promedio
con = 0
con_pasaron = 0
con_nopasaron = 0
suma = 0

while(con <=2):
  nota = float(input('escribir nota'))
  if (nota>=3.0):
    print('Aprobo')
    con_pasaron = con_pasaron + 1
  else:
    print('no aprobo')
    con_nopasaron = con_nopasaron + 1
  suma = suma + nota
  con = con+1
prom = 4suma/3
print(prom)
print(f'Pasaron {con_pasaron} no pasaron {con_nopasaron}')
x

# pedir 5 numeros y sumarlos y calculuar su promedio, contar los mayores y los menores de 10

con = 1
suma = 0
con_mayor10 = 0
con_menor10 = 0

while(con<= 5):
  numero = float(input(f'Escribir numero {con}'))
  if(numero<=10):
    con_menor10 = con_menor10 +1
  else:
    con_mayor10 = con_mayor10 +1
  suma = suma + numero
  con = con + 1
prom = suma/5
print(f'El promedio es {prom} , la cantidad de numeros menor de 10 es: {con_menor10}, la cantidad de numeros mayores de 10 es: {con_mayor10}')




# Clave

numero = 1
while(numero != 0):
  numero = int(input('Ingrese clave'))
  if (numero != 0):
    print('Clave erronea')
  else:
    print('Clave exitosa')


# Ciclo for

for i in range(1,10):
  print('i ',end="")
  print(2)

"""
# mostrar numeros del 1-20
for i in range(20, -1 ,-1):
    print(i)
