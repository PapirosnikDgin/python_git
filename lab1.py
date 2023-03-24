from math import *

def perimetr( n:int, r:float ):
   return 2*r*n*tan(pi/n)

n=int(input("Введите число углов n-угольника: "))
r=float(input("Введите радиус описанной окружности : "))

assert abs(perimetr(4,2) - 16) < 1e-8 
print("P:", perimetr(n,r))
