import my_module as mm
import numpy as np

__author__ = "Номокoнов"

row =int(input("\nВведите количество строк матрицы: "))
col =int(input("Введите количество столбцов матрицы: "))

a= np.random.uniform(0,100,(row,col))
print("\nматрица:\n",a)
mm.print_matrf(a)