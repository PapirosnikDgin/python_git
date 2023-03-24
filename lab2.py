from math import *

a=float(input("Введите a : "))
b=float(input("Введите b : "))
c=float(input("Введите c : "))

if(a>=b>=c):
   a*=2
   b*=2
   c*=2
else:
   a=abs(a)
   b=abs(b)
   c=abs(c)

print(f"a: {a:5.2f}")
print(f"b: {b:5.2f}")
print(f"c: {c:5.2f}")