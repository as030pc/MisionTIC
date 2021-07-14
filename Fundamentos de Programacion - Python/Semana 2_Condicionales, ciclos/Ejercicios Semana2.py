
# Tcelcius = float(input('Ingrese la temperatura:'))
# Tkelvin = Tcelcius + 273.15
# print(f'La temperatura {Tcelcius} °C equivale a {Tkelvin} K')
#
#
# # Elabore programa en Python que lea dos datos enteros correspondientes a los catetos de un triángulo rectángulo y que calcule e imprima el valor de la hipotenusa de dicho triángulo.
# num = int(input('Ingrese un numero entero'))
#
#
# # Elabore programa en Python que imprima la suma de los números enteros de 300 hasta 5000
#
#
#
# # Elabore un programa en Python que lea un entero de tres dígitos y produzca como salida los dígitos del número leído
#
num = int(input('Ingrese un numero entero'))


for i in range(2,-1,-1):
    digito = num//(10**i)
    num = num%(10**i)
    print(digito)

