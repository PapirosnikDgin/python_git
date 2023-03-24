import my_module as mm
import math
import numpy as np

__author__ = "Номокoнов"

row =int(input("\nВведите количество строк матрицы: "))
col =int(input("Введите количество столбцов матрицы: "))

a= np.random.uniform(0,100,(row,col))
#print("\nматрица:\n",a)

#a=mm.create_matr(row,col)
mm.print_matrf(a)
b=mm.count_if2(a)
#print("\n",a[3:a.shape[0],:3].sum())
#print("\n",sum(a[3:a.shape[0],:3]))
mm.print_matrf(b)