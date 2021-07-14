"""OPERACIONES CON DIGITOS """

"""recibe 2 cadenas y compara digito a digito:
cad1=1543
cad2=1060  
rdo: 1-5-10-3
si los digitos son 1 o 0 el resultaado es 1
de lo contrario se suman

"""
def sumarDigitos(dig1,dig2):
    if( (dig1=="1" and dig2=="1") or (dig1=="0" and dig2=="0")):
        return "1"
    else:
        return str(int(dig1)+int(dig2))

"""recibe 2 cadenas y compara digito a digito:
cad1=1543
cad2=1060  
rdo:0,5,-2,3,
si los digitos son 1 o 0 el resultaado es 9
de lo contrario se restan

"""
def restarDigitos(dig1,dig2):
    if( (dig1=="1" and dig2=="1") or (dig1=="0" and dig2=="0")):
        return "0"
    else:
        return str(int(dig1)-int(dig2))


def solucion(cad1,cad2,op):
    rdo = ""

    if(op=="sumar"):
        for i in range(len(cad1)):
            rdo += sumarDigitos(cad1[i], cad2[i]) + "-"
    elif (op=="restar"):
        for i in range(len(cad1)):
            rdo += restarDigitos(cad1[i], cad2[i]) + ","
    else: return "opcion no valida"

    return rdo




cad1="1543"
cad2="1060"
print(solucion(cad1,cad2,"sumar"))
print(solucion(cad1,cad2,"restar"))