def soloVer():
    print("hola desde subprograma")

def devolverDato():
    a=20
    b=30
    r=a+b
    print("devolviendod dato")
    return r

def enviaryVer(x):
    r=x**2
    print(r)

def enviaryDevoler(x):
    r=x**2
    return r

print("")
soloVer()
n=10
a=enviaryDevoler(n)
print(a)