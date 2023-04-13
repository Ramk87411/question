# sum of a given range

first_num = int(input("Enter your first numnber: "))
second_num = int(input("Enter your second numnber: "))

sum = 0
for i in range(first_num,second_num+1):
    sum += i
print(sum)