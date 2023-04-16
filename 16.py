# find the nth term of fibonacci series
# create direct last term of series

user_num = int(input("enter your number: "))

def fibonacci(user_num):
    if user_num<=1:
        return user_num
    else:
        return fibonacci(user_num-1)+fibonacci(user_num-2)

print(fibonacci(user_num))
