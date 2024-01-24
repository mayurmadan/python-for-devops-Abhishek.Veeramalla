#if elif else
x = int(input("enter a number:"))

if x % 2 == 0 :    
    print("this is a even number & its raised to power 2 is", (x ** 2))
elif x % 2 != 0 :
    print("this is a odd number & its raised power to 3 is:", (x ** 3))


#nested if example
age = int(input("enter your age:"))
height = float(input("enter your height:"))

#greater than and equval to 18 and smaller than and 24
if 23 >= age >= 18  :
    if height >= 5.9:
        print("your are eligibale for army, without donation")
    else:
        print("you are eligible with donation")
else:
    print("you are not allowd here")         
    
