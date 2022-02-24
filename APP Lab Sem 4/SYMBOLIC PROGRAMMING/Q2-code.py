"""2. Develop a python code for to carryout the operations on the given algebraic 
manipulation for the given expression a2−ab+ab−b2=a2−b2 by using the symbolic programming paradigms principles"""

#Q2
import sympy as sym
a = sym.Symbol('a')
b=sym.Symbol('b')
sym.simplify(a**2 -a*b +a*b -b**2)
