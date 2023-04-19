# Automorphic number : A number is called an automorphic number if and only if the square of the given number ends with the same number itself. For example, 25, 76 are automorphic


num = int(input("enter your number: "))

square = num*num

num_string = str(square)
square_string = str(square)

if square_string.endswith(square_string):
    print(f"{num} is a armstrong number")
else:
    print(f"{num}  is not a armstong number ")