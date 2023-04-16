# factor of  a number

num = int(input("enter your number: "))

fact = ""
for i in range(1, num+1):
    if num % i == 0:
        fact = fact+ str(i)+ ","


print(f"factorial of {num} is : {fact}")