# Perfect number  =  a positive integer that is equal to the sum of its proper divisors. The smallest perfect number is 6, which is the sum of 1, 2, and 3. Other perfect numbers are 28, 496, and 8,128.


num = int(input("enter your number: "))

list = []
for i in range(1,num):
    if num % i == 0:
        list.append(i)
print(list)

sum = 0
for i in list:
    sum += i
print(sum)

if sum == num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")