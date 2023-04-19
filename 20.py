# Find the Prime Factors of a Number in Python

num = int(input("enter your number: "))

list = []
prime_divisor = 2

while prime_divisor <=num:
        if num % prime_divisor ==0:
            list.append(prime_divisor)
            num = num/prime_divisor
        else:
            prime_divisor += 1

print(f"prime factor of number is : {list}")