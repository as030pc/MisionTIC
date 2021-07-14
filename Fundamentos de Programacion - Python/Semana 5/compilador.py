from Pilas import Pila

"""Verificar cadena de parentesis ()"""
def verificarParentesis(cadenaSimbolos):
    p = Pila()
    balanceados = True
    indice = 0
    while indice < len(cadenaSimbolos) and balanceados:
        simbolo = cadenaSimbolos[indice]
        if simbolo == "(":
            p.apilar(simbolo)
        else:
            if p.estaVacia():
                balanceados = False
            else:
                p.desapilar()

        indice = indice + 1

    if balanceados and p.estaVacia():
        return True
    else:
        return False

"""verificacion completa con {[( """
def verificarFull(simbolos):
    p = Pila()
    balanceados = True
    indice = 0
    while indice < len(simbolos) and balanceados:
        simbolo = simbolos[indice]
        if simbolo in "([{":
            p.apilar(simbolo)
        else:
            if p.estaVacia():
                balanceados = False
            else:
                tope = p.desapilar()
                if not parejas(tope,simbolo):
                       balanceados = False
        indice = indice + 1
    if balanceados and p.estaVacia():
        return True
    else:
        return False

def parejas(simboloApertura, simboloCierre):
    aperturas = "([{"
    cierres = ")]}"
    return aperturas.index(simboloApertura) == cierres.index(simboloCierre)


# lp=['(','(',')',')',')']
cad="(()"

print(verificarParentesis("((()))"))
print(verificarFull('{{([][])}()}'))
