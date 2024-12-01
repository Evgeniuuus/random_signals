import numpy as numpy


def Rxx(x):
    m = numpy.mean(x)
    return [1 / (len(x) - k) *
            sum([(x[i] - m) * (x[i + k] - m) for i in range(len(x) - k)]) for k in range(16)]


def Rxy(x, y):
    mx = numpy.mean(x)
    my = numpy.mean(y)
    return [1 / (len(x) - k) *
            sum([(x[i] - mx) * (y[i + k] - my) for i in range(len(x) - k)]) for k in range(16)]


"""
Rxx(x) вычисляет автокорреляцию для ряда 
            (т.е. как ряд связан с его сдвигами)

Rxy(x, y) вычисляет кросс-корреляцию между двумя рядами 
            (т.е. насколько значения одного ряда связаны с сдвигами другого ряда)
"""
