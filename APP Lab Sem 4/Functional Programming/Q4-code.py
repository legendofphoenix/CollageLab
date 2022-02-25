"""4. Closure
A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory. We have a closure in Python when a nested function 
references a value in its enclosing scope.
a. Study the following program by executing it:
def multiplier_of(n):
def multiplier(number):
return number*n
return multiplier
multiplywith5 = multiplier_of(5)
print(multiplywith5(9))
b. In a lottery system, random number is chosen by retrieving the number from a random
index from a list of random numbers. Write a program to choose a random number in this
way. You must use nested functions – the inner function chooses a number from a random
index and the outer function generates a random list of numbers. The outer function takes
n as a parameter where is the maximum number that can be put in the random list.
"""
# 4A
def multiplier_of(n):
    def multiplier(number):
            return number*n
    return multiplier
multiplywith5 = multiplier_of(5)
print(multiplywith5(9))

#4B

import random
m=10
print("Let the maximum limit for generating random numbers be "+str(m))
lst=[]
for i in range(m):
    lst.append(random.randint(1,m)) 
for j in range(1):
    d1=random.randrange(0,m,1)
    print("Index of the random number is ",lst[d1])
print("\n")
