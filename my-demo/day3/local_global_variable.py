#this function work anywher in this code
x = int(input("enter a number:"))
y = 15

##local varibale 
def sum():
    #this vraible is work within this function only 
    a = 10 
    b= 11
    print(a + b)

  #now call th function
sum()

##global varaiable 
def diff():
    print(x + y)

diff()    
