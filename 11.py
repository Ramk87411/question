# sum of a digit of a number 

num = int(input("enter a num: "))

# sum  = 0
# for i in num:
#     sum  = sum+ int(i)

# print(sum)
sum = 0

while num != 0:
    rem = num % 10
    sum += rem
    num = num//10
    
print(sum)