# prime number 

user_num = int(input("Enter your number: "))
flag = 0
for i in range(2,user_num):
    if user_num%i == 0:
        flag = 1


if flag==1:
    print("Not a prime")
else:
    print("Prime number")