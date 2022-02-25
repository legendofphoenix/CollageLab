"""2. Lambda functions
a. Write a lambda function to convert measurements from meters to feet.
b. Write a lambda function in Python to implement the following lambda expression:
(λf. λm. (f + m)a)(λx. x2)(b)
Note: You need to write a nested lambda function for implementing f+m where f takes the square function (which takes argument x) passed as a parameter. The above expression calculates a2+b.
"""
def multiplier_of(n):
    def multiplier(number):
            return number*n
    return multiplier
multiplywith5 = multiplier_of(5)
print(multiplywith5(9))
