import numpy # импортируем библиотеку

from data_for_array import *


M = numpy.array(A) # Матрица (левая часть системы)
v = numpy.array(B) # Вектор (правая часть системы)kkl

print(numpy.linalg.solve(M, v))
