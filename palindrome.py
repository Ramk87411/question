# palindrome 

user_num = int(input("Enter your number: "))


num = user_num
reverse = 0
while user_num!=0:
    rem = user_num % 10
    reverse = (reverse*10) + rem
    user_num = user_num // 10
print(reverse)

if num == reverse:
    print("palindrome")
else:
    print("not palindrome")

"""
Note:-
In the given code, num = user_num step is used to store the original input number before performing the reverse calculation.

This is important because, during the reverse calculation, the value of user_num is changed as each digit is extracted and processed. Without storing the original input in a separate variable, it would not be possible to compare the original input number with the reversed number to determine if it is a palindrome.

Therefore, num = user_num step allows us to preserve the input value and use it later for comparison with the reversed number to determine whether the input number is a palindrome or not."""


