import csv

archivo=open("GOOG.csv", "r")
datos=csv.DictReader(archivo,delimiter=",")
datos_salida =  []
fila = []
date_lowest_mean = ''
lowest_mean = 20000
date_highest_mean = ''
highest_mean = -20000
for i in datos:
    fila.append(i['Date'])
    if float(i['Adj Close']) < 1624:
        fila.append('MUY BAJO')
    elif float(i['Adj Close']) >= 1624 and float(i['Adj Close']) < 1854:
        fila.append('BAJO')
    elif float(i['Adj Close'])>= 1854 and float(i['Adj Close']) < 2084:
        fila.append('MEDIO')
    elif float(i['Adj Close']) >= 2084 and float(i['Adj Close']) < 2314:
        fila.append('ALTO')
    elif float(i['Adj Close']) >= 2314:
        fila.append('MUY ALTO')
    datos_salida.append(fila)
    fila = []
    prom = (float(i['High'])+float(i['Low']))/2
    if prom > highest_mean:
        highest_mean = prom
        date_highest_mean = i['Date']
    if prom < lowest_mean:
        lowest_mean = prom
        date_lowest_mean = i['Date']


encabezado = ['Fecha', 'Concepto']
with open("analisis_archivo.csv", "w", newline="", encoding="utf-8") as archivo:
    escritor=csv.writer(archivo, delimiter="\t")
    escritor.writerow(encabezado)
    escritor.writerows(datos_salida)

