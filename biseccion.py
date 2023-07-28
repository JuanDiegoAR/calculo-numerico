import math
def biseccion(f, a, b, es, max_i):
    ea = 100
    i = 0
    m_actual = 0
    m_previa = 0
    
    if (f(a) * f(b)) >= 0:
        print("No se puede aplicar el metodo de biseccion ya que no se cumple la 2da condicion del teorema")
    else:
        while (i < max_i) and (ea > es):
            m_previa = m_actual
            m_actual = (a + b) / 2

            if f(m_actual) * f(b) < 0:
                    a = m_actual
            else:
                b = m_actual
                
            if (i > 1):
                ea = abs((m_actual - m_previa) / m_actual)

            i += 1

        print("El punto medio actual es: ", m_actual)
        print("El error aproximado relativo es", ea)
        print("El número de iteraciones es de: ", i)
        return m_actual
    