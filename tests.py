import unittest
import math
from biseccion import biseccion
from integracion_numerica import *
from newton_raphson import *

class TestBiseccion(unittest.TestCase):
    def test_biseccion(self):
        f = lambda x: math.exp(x) - (3*(x**2))
        a = 0
        b = 1
        es = 0.03
        max_i = 20
        raiz_esperada = 0.921875
        raiz_calculada = biseccion(f, a, b, es, max_i)
        self.assertAlmostEqual(raiz_calculada, raiz_esperada, delta=es)
    
    def test_valor_intermedio(self):
        f = lambda x: math.exp(x) - (3 * (x ** 2))
        a = 0
        b = 1
        max_i = 20
        es = 0.03
        self.assertTrue(f(a) * f(b) < 0)

class TestNewtonRaphson(unittest.TestCase):

    def test_newton_raphson_simple(self):
        f = lambda x: x**2 - 4
        a = 0
        b = 5
        es = 0.01
        max_i = 20
        self.assertAlmostEqual(newton_raphson(f, a, b, es, max_i), 2.0, delta=0.01)


class TestSumaRiemann(unittest.TestCase):

    def test_suma_riemann_constante(self):
        f = lambda x: 5
        a = 0
        b = 10
        n = 50
        self.assertEqual(suma_riemann(f, a, b, n), 50.0)

    def test_suma_riemann_no_lineal(self):
        f = lambda x: x ** 2
        a = 0
        b = 1
        n = 100
        self.assertAlmostEqual(suma_riemann(f, a, b, n), 1/3, delta=0.01)

class TestMetodoTrapecio(unittest.TestCase):

    def test_metodo_trapecio_constante(self):
        f = lambda x: 5
        a = 0
        b = 10
        n = 50
        self.assertAlmostEqual(metodo_trapecio(f, a, b, n), 50.0, delta=0.01)

    def test_metodo_trapecio_no_lineal(self):
        f = lambda x: x ** 2
        a = 0
        b = 1
        n = 100
        self.assertAlmostEqual(metodo_trapecio(f, a, b, n), 1/3, delta=0.01)

if __name__ == '__main__':
    unittest.main()