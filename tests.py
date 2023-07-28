import unittest
import math
from biseccion import biseccion

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


if __name__ == '__main__':
    unittest.main()