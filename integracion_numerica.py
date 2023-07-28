import math

def suma_riemann(f, a, b, n):
    h = (b-a)/n
    acum = 0
    for i in range(n):
        x = a + i * h
        acum = acum + h * f(x)
    return abs(acum) 


def metodo_trapecio(f, a, b, n):
    h = (b-a)/n
    acum = 0
    for i in range(n):
        x = a + i * h
        x1 = x + h
        acum = acum + ((f(x) + f(x1))*h)/2 
    return abs(acum)

f = lambda x: math.sqrt(x+1)
a=1
b=-1
n=5

print(metodo_trapecio(f, a, b, n))
    
    