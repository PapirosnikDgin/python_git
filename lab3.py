from math import *

print("Введите координаты клеток: ")

print("\nПервая клетка:")
a=int(input("Введите a (1-8) : "))
b=int(input("Введите b (1-8) : "))

print("\nВторая клетка:")
a1=int(input("Введите a1 (1-8) : "))
b1=int(input("Введите b1 (1-8) : "))

if((a+b)%2==(a1+b1)%2):
   print("\nЦвет клеток одинаковый")
   if((a+b)%2==0):
      print("Белые кетки")
   else:
      print("Черные клетки")
else:
   print("\nЦвет клеток разный")


