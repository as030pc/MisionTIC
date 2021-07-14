lista = [1,2,45,6]
# n = len(lista)
# print(n)
#
# lista.append(9)
# print(lista)
#
# lista.insert(3, 3)
# print(lista)
#
# lista.pop() #elimina el ultimo dato
# print(lista)
#
# lista.pop(1)
# print(lista)
#
# ind = lista.index(45) # Busca el indice donde esta el numero
# print(ind)
#
# m = lista.count(9) # Numero de veces que repite ese numero
# print(m)
#
#
# lista.reverse() #poner al reves
# print(lista)
#
# lista.sort() # ordena la lista en orden ascendente
# print(lista)
#
# lista.sort(reverse = True) # Ordena de forma ascendente
# print(lista)
#
lista2 = lista.copy()
# print(lista2)
#
# lista.clear() #Borra todo lo de la lista
# print(lista)
lista.extend(lista2)
print(lista)

del lista[1] # Borra en una posicion dada
print(lista)

lista.remove(45) #Borra un elemento
print(lista)

#Rangos
print(lista[0:3])  #No coge la ultima posicion
del lista[0:3] #Borra un rango
print(lista)

del lista[2:] #Desde la posicion 2 hasta el final




