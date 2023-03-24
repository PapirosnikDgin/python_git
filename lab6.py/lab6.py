import my_module as mm
import math

__author__ = "Номокoнов"

n=int(input("Введите длину массива: "))
#if1=int(input("Введите число на которое делятся элементы: "))
#if2=int(input("Введите число на которое  не делятся элементы: "))

a=mm.create_mass_int(n)
print("\n массив:",a)
print(f"\nРезультат:",mm.count_if(a,lambda x: x%3==0 and x%5!=0))

# s=0

# for i in range(0,n):
#     if a[i]%3==0 and a[i]%5!= 0:
#         s+=1
#print(f"\nРезультат:",s)


