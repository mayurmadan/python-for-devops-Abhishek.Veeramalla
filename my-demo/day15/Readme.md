##DECORATOR 
In Python, a decorator is a way to modify or enhance the behavior of functions or methods without changing their actual code. It allows you to wrap another function and execute code before and after the wrapped function runs.
#EXAMPLE
# Define a decorator function
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()  # Call the original function
        print("Something is happening after the function is called.")
    return wrapper

# Define a function and apply the decorator to it
@my_decorator
def say_hello():
    print("Hello!")

# Call the decorated function
say_hello()
 #Output:
Something is happening before the function is called.
Hello!
Something is happening after the function is called.

