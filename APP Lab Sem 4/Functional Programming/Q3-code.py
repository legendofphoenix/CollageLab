"""3. Passing and returning a function as an argument
Define a function ‘square’ for squaring a number. Define a function named ‘twice’ that takes a function f as an argument and returns f(f(x)). Using ‘twice’ and 
‘square’ create a function ‘quad’ that takes n as an argument and returns n4 ‘quad’ should not be defined explicitly. It should only be created as a variable which
is then assigned a function.
"""


def square(number): 
    value = number * number
    return value
def twice(func,num):
    return func(func(num))
n=int(input('Enter a number:'))
k=twice(square,n)
print(k)
