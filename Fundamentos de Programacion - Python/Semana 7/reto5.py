import pandas as pd
import csv


data = pd.read_csv('GOOG.csv')
print(data)
a = []
for row in data:
    a = a.append(row)

print (a)
#

fecha = data.Date
grande = data.High
datos = [fecha, grande]


datos_salida = pd.DataFrame(data = datos)

print(datos_salida)
print(fecha[1])
print (a)