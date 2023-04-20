#  Harshad number  == A positive integer which is divisible by the sum of its digits, also called a Niven number (Kennedy et al. 1980) or a multidigital number (Kaprekar 1955). The first few are 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 18, 20, 21, 24, ... (OEIS A005349). Grundman (1994) proved that there is no sequence of more than 20 consecutive Harshad numbers, and found the smallest sequence of 20 consecutive Harshad numbers, each member of which has 44363342786 digits.

num = int(input("enter your number: "))

list = []
temp = num
while temp>0:
    rem = temp%10
    list.append(rem)
    temp = temp//10
print(list)

sum = 0
for i in list:
    sum += i
print(sum)

if num%sum ==0:
    print(f"{num} harshad number ")
else:
    print(f"{num} is not a harshad number ")