#here test is function name & name is input or argument of function
def test(name):
    #here we use f string to add varibale or iteral into string literal
    
    print(f"my name is {name}")
     
#here calling the function and arugument provided is mayur so it replace name with mayur  and print it as we call function
test("mayur") 

#again calling same function with new input
test("sachine")

#example2 with return
def addition(x,y):
    #this adding number x and y when we caaling this function and pass the argument or input
    return x + y

berij = addition(12,10)
print(f"addtion is,{berij}")

#example 
print("addition is",addition(12,13))


###########################################################
#sample example
def even_number(num):
    return num % 2 == 0
def odd_number(num):
    return num % 2 != 0
def get_squre(num):
    return num ** 2

#now using above function
num = int(input("enter a number\n:"))

if even_number (num):
    print(f"{num} is even number")
else:
    #get_squre only if num is even 
    square_is = get_squre(num)
    print(f"{num} is a odd number")
    print(f"{num} squre is:{square_is}")


