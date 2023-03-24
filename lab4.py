
__author__ = "Номокoнов"

n=int(input("Введите количетсво слагаемых: "))

#a=[1/i for i in range(1,n+1)]        #генератор списка
#print("массив: \n",a)

s = 0
print("элементы:")
for i in range(1,n+1):
 print(f"{i}:",1/i)
 s+= 1/i
print(f"\nсумма: {s:.3f}",)

#print("\nсумма массива(#1):",sum(a))
