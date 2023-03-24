import my_module as mm
import math

__author__ = "Номокoнов"

n=int(input("Введите длину массива: "))
s = 0

print("элементы:")

for i in range(1,n+1):
 print(f"{i}:",1/math.factorial(int(math.pow(i,2))))
 s+= 1/math.factorial(int(math.pow(i,2)))
 
print(f"\nсумма массива(#2): {s:.3f}",)


