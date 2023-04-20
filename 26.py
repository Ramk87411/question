#Abundant number == In number theory, an abundant number or excessive number is a number for which the sum of its proper divisors is greater than the number. The integer 12 is the first abundant number. Its proper divisors are 1, 2, 3, 4 and 6 for a total of 16. The amount by which the sum exceeds the number is the abundance

num = int(input("Enter your number: "))
print(num)
list = []
temp = num
for i in range(1,temp):
    if temp%i == 0:
        list.append(i)

print("divisor of num " , list)

sum = 0
for i in list:
    sum += i
print("Sum of divisor is",sum)

if sum > num:
    print(f"{num} is abundant number ")
else:
    print(f"{num} is not abundant number ")