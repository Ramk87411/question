# prime number within a given range 

num_1 = int(input("Enter  your first number: "))
num_2 = int(input("Enter  your second number: "))

def is_prime(num_1,num2):
    for i in range(num_1,num_2+1):
        if i > 1:
            for j in range(2,i):
                if i%j == 0:
                    break
            else:
                print(i)

is_prime(num_1,num_2)