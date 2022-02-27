""" Symbolic Programming Paradigm
1. Solve the following using symbolic paradigm:
i. Calculate sqrt (2) with 100 decimals"""

#Q1a
from sympy import *
(sym.sqrt(2)).evalf(100)
#Q1a
from sympy import *
(sym.sqrt(2)).evalf(100)

# 1.414213562373095048801688724209698078569671875376948073176679737990732478462107038850387534327641573

# ii. Calculate (1/2+1/3) in rational arithmetic.

#Q1b
import sympy as sym
a = sym.Rational(1,2)
b=sym.Rational(1,3)
c = a+b
print(c)

#5/6

#iii. Calculate the expanded form of (x+y) ^ 6.

#Q1c
x = sym.Symbol('x')
y = sym.Symbol('y')
sym.expand((x+y)**6)

# 𝑥6+6𝑥5𝑦+15𝑥4𝑦2+20𝑥3𝑦3+15𝑥2𝑦4+6𝑥𝑦5+𝑦6

# iv. Simplify the trigonometric expression sin (x) / cos (x)

#Q1d
exp = sin(x)/cos(x)
res=sym.trigsimp(exp)
print(res)

#tan(x)

# v. Calculate sin x -x^3

#Q1e
n=sym.Symbol('n')
print(simplify(sin(x)-x**3*n))   
print("\n")

# -n*x**3 + sin(x)


""" 2.Develop a python code for to carryout the operations on the given algebraic manipulation for the given expression a2−ab+ab−b2=a2−b2 by using the symbolic
programming paradigms principles."""

#Q2
a = sym.Symbol('a')
b=sym.Symbol('b')
sym.simplify(a**2 -a*b +a*b -b**2)

#𝑎2−𝑏2
#Give the Symbolic program for the expression given below:
#a. ∬a2 da

#Q3a
a = sym.Symbol('a')
b=sym.Symbol('b')
sym.integrate(sym.integrate(a**2,a))

#𝑎412
3b. 2x+y2

#Q3b
x = sym.Symbol('x')
y = sym.Symbol('y')
sym.simplify(2*x + y**2)

# 2𝑥+𝑦2
# c. 1/10 + 1/5

#Q3c
sym.Rational(1,10)+sym.Rational(1,5)

# 310
# d. d/dx(sin(x))

#Q3d
x=sym.Symbol('x')
sym.diff(sym.sin(x),x)

# cos(𝑥)
