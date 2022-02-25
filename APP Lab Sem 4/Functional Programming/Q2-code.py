"""2. Lambda functions
a. Write a lambda function to convert measurements from meters to feet.
b. Write a lambda function in Python to implement the following lambda expression:
(λf. λm. (f + m)a)(λx. x2)(b)
Note: You need to write a nested lambda function for implementing f+m where f takes the square function (which takes argument x) passed as a parameter. The above expression calculates a2+b.
"""
#Qn 2a
feet = lambda m: m*(3.281)
meters = int(input("Enter the number of meters to be converted: "))
print("{:0.2f} feet".format(feet(meters)))



square = lambda x: x**2
total = lambda f, b: lambda a: f(a)+b
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
print(total(square, b)(a))
