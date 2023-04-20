# friendly pair == Two numbers with the same "abundancy" form a friendly pair


def divisosr_sum(num):
    sum = 0
    for i in range(1,num):
        sum += i
    return sum

def is_abundant(num):
    return divisosr_sum(num) > num
def is_friendly(num_1,num_2):
    return divisosr_sum(num_1) == divisosr_sum(num_2)
num_1 = int(input("Enter your 1st number: "))
num_2 = int(input("Enter your 2nd number: "))

if is_abundant(num_1):
    print(f"{num_1} is abundant number")
else:
    print(f"{num_1} is not a abundant number")

if is_abundant(num_2):
    print(f"{num_2} is abundant number")
else:
    print(f"{num_2} is not a abundant number")

if is_friendly(num_1,num_2):
    print(f"{num_1} and {num_2} form a friendly pair")
else:
    print(f"{num_1} and {num_2} form a friendly pair")
