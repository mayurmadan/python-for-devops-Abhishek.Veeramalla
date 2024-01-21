#####################
#this is module file containeing the functions for math
def even_number(num):
    return num % 2 == 0
def odd_number(num):
    return num % 2 != 0
def get_squre(num):
    return num ** 2

#addition function for add & divide
def add(x,y):
    return x+y

def divide(x,y):
    if y != 0:
        return x/y
    else:
        print("Error: cannot divide by zero")
        
