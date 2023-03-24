import my_module as mm
import math

__author__ = "Номокoнов"

n=int(input("Введите длину массива: "))
a=mm.create_mass_double(n)
mm.print_masf(a)
print(f"\nРезультат: {mm.calc_f1(a,n):.2f}")


