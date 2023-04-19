#Strong number = sum of factorial of digit in number is equal to number 
# 145 is strong number. Since, 1! + 4! + 5! = 145. 
# 1! = 1
#2! = 2 

num = int(input("enter your number: "))
list = []
temp = num
while temp > 0:
    rem = temp % 10 
    list.append(rem)
    temp = temp // 10 
# list.reverse()
# print(list)
list.reverse()
sum  = 0
for value in list:
    factorial_val = 1
    for i in range(1,value+1):
        factorial_val *= i
    sum += factorial_val
if sum == num:
    print(f"{num} is a strong number ")
else:
    print(f"{num} is not a strong number")