# import random
# mat = [[1,2], [2,7]]
#
# lista = [5,8, 10]
#
# for i in mat: #Impresion de una matriz
#     print(i)
#
# #Creacion de una matriz vacia
#
# mat2 = []
# for i in range(3):
#     a = [0]*2
#     mat2.append(a)
#
# print(mat2)
# print(len(mat2)) #numero de filas
# print(len(mat2[0])) #numero de columnas
# for i in range(0,len(mat2)):
#     for j in range(0, len(mat[0])):
#         #print(mat2[i][j], end= "")
#         mat2[i][j] = random.randint(1,10)
#     print('')
# print(mat2)


#Creacion de matrices

m1 = [[2,7], [8,5]]
m2 = [[2,7,3],[8,5,21],[4, 4, 12]]
m3 = [[8,5,21,4],[4,6,12,2],[9,2,4,35],[7,16,28,39]]
print(m1)
print(m2)
print(m3)

#Recorrido de matrices

#Recorrido por filas
m = len(m3)
for i in range(0, m):
    for j in range(0,m):

        print(m3[i][j], end = "\t")
    print()


#Diagonal principal
m = len(m3)
suma = 0
for i in range(0, m):
    for j in range(0,m):
        if (i ==j):
            suma = suma+ m3[i][j]
            #print(m3[i][j], end = "\t")
print(suma)

#Debajo de la diagonal i> j


for i in range(0, m):
    for j in range(0,m):
        if (i >j):
            print(m3[i][j], end = " ")
    print()

#Debajo de la diagonal i< j
for i in range(0, m):
    for j in range(0,m):
        if (i <j):
            print(m3[i][j], end = " ")
    print()

#Diagonal secundaria

for i in range(0, m):
    for j in range(0,m):
        if (i+j == m-1):
            print(m3[i][j], end = " ")

    print()



# Contar los pares
cont=0
for i in range(0, m):
    for j in range(0,m):
        if ((m3[i][j])%2 ==0):
            cont+=1
    print()
print(cont)