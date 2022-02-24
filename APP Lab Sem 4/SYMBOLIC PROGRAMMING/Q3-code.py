""" 3. Give the Symbolic program for the expression given below:
a. a2 da
b. 2x+y2 c. 1/10 + 1/5
d. d/dx(sin(x))"""
#i) integrate a^2
import sympy as sym
a = sym.Symbol('a')
b=sym.Symbol('b')
sym.integrate(sym.integrate(a**2,a))

#ii) 2x+y^2
import sympy as sym
x = sym.Symbol('x')
y = sym.Symbol('y')
sym.simplify(2*x + y**2)

#iii) 1/10 + 1/5
sym.Rational(1,10)+sym.Rational(1,5)

#iv) d/dx(sin(x))
x = symbols('x')
print(diff(sin(x)))
