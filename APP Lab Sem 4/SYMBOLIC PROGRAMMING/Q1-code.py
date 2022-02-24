""" 1. Solve the following using symbolic paradigm:
i. Calculate sqrt (2) with 100 decimals.
ii. Calculate (1/2+1/3) in rational arithmetic.
iii. Calculate the expanded form of (x+y) ^ 6.
iv. Simplify the trigonometric expression sin (x) / cos (x)
v. Calculate sin x -xx^3n"""

from sympy import *
#i) Calculate sqrt (2) with 100 decimals
print(N(sqrt(2)*1,100))

#ii) Calculate (1/2+1/3) in rational arithmetic
a=Rational(1,2)
b=Rational(1,3)
print(a+b)

#iii) Calculate the expanded form of (x+y) ^ 6.
import sympy as sym
x = sym.Symbol('x')
y = sym.Symbol('y')
sym.expand((x+y)**6)

#iv) Simplify the trigonometric expression sin (x) / cos (x)
print(simplify(sin(x)/cos(x)))

#v) Calculate sinx-xx^3n
print(simplify(sin(x)-x**3*n))
