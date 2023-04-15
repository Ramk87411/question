# armstrong number
# 1 => 1^1 = 1 (1 is Armstrong Number)

# 2 => 2^1 = 2 (2 is Armstrong Number)

# 9 => 9^1 = 9 (9 is Armstrong Number)

# 10 => 1^2 + 0^2 = 1 + 1 = 2 (10 is not Armstrong number)

# 153 => 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153 (153 is Armstrong number).


num = int(input("enter your number: "))
length = len(str(num))
sum = 0
temp = num
while temp > 0:
    rem = temp % 10
    sum = sum + rem ** length
    temp = temp//10
if num == sum:
    print( f"{num} is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
