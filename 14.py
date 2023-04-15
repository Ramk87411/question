# armstrong number in a given range 

num_1 = int(input("Enter  your first number: "))
num_2 = int(input("Enter  your second number: "))


for i in range(num_1,num_2+1):
    num = i
    length = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        rem = temp % 10
        sum = sum + rem ** length
        temp = temp//10
    if i == sum:
        print( i)
            
