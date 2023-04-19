# Perfect Square

"""
num = int(input("enter your number, which you want to check a perfect square or not : "))

list = []
for i in range(1,num):
    if num % i ==0 :
        list.append(i)
# print(list)

is_perfect_square = True
for i in list:
    if i**2 ==num :
        is_perfect_square = True
        print("perfect square")
"""


import math
num = int(input("enter your number: "))

value = math.sqrt(num)
int(value)
print(value)

if value**2== num:
    print("perfect square")
else:
    print("Not a perfect square")