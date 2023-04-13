# greatest of three

num_1 = int(input("Enter your num1: "))
num_2 = int(input("Enter your num2: "))
num_3 = int(input("Enter your num3: "))

if num_1 >= num_2:
    if num_1 >= num_3:
        print(num_1)
elif num_2 >= num_1:
    if num_2 >= num_3:
        print(num_2)
    else:
        print(num_3)