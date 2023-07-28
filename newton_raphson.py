import math

def dx(f, h):
    def R(x):
        return (f(x + h) - f(x))/h
    return R

def newton_raphson(f, a, b, es, max_i):
    ea=100
    i=0
    fdx = dx(f, 0.0000002)
    x0 = (a + b)/2
    x1 = x0 - (f(x0) / fdx(x0))

    while (i < max_i) and (ea > es):
        x0 = x1
        x1 = x0 - (f(x0) / fdx(x0)) 
        ea = abs((x1 - x0) / x1)
        i += 1
    
    print("El ultimo x es: ", x1)
    print("El error aproximado relativo es: ", ea)
    print("El número de iteraciones es de: ", i)
    return x1

f = lambda x: math.exp(x) - (3*(x**2))
a = 0
b = 1
es = 0.02
max_i = 20

newton_raphson(f, a, b, es, max_i)

