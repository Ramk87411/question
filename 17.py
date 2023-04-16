# factorial of a number 

num = int(input("Enter your number: "))

val =1
fact = ""
for i in range(1,num+1):
    val  = val*i
    if i < num:
        fact = fact + str(i)+"*"
    else:
        fact = fact + str(i) + "="
    
print(f"factorial of {num} is: {fact} {val}")