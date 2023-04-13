# sum of first n natural number 

user_num = int(input("Enter your number: "))

# for i in range(0,user_num+1):
#     print ((i*(i+1))/2)
sum = 0
for i in range(user_num+1):
    sum += i
print(sum)