#factorial of a number is the product of all positive integers up to that number, including the number itself.
#For example, the factorial of 5 (written as 5!) is calculated as:
# 5!=5×4×3×2×1=120

num = int(input("Enter a number: "))
fact = 1
i = 1

while i <= num:
    #means fact = fact * i  
    fact *= i
    i += 1

print(f"The factorial of {num} is: {fact}")
