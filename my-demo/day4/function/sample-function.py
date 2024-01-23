num1= 10
num2 = 5

#without function 
add = print(num1+num2)
#using string concatination , it is support only string concatination
adding = num1 + num2
print("sum of numbers -" + str(adding))

sub = print(num1-num2)

##### With Function ######
def add ():
    addition = num1 + num2
    print(f"addition using function:",(addition))

def sub():
    print(f"sub of numbers:", (num1 - num2))

def mul(num1,num2):
    #print(f"multi for num is:",(num1 * num2))
    return(num1*num2)
def divide(num1,num2):
    return(num1 // num2)
#now calling the functions, we have to call function to execute it
#sub fucnction
sub()

#mul function
print(mul(10,10))

#divide function
num1 = int(input("enter the num1:"))
num2 = int(input("enter num2:"))
print(f"divide is ",(divide(num1,num2)))
