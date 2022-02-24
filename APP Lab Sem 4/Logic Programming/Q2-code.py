"""
2. Encode the following facts and rules in pyDatalog: • Bear is big
	Elephant is big
	Cat is small • Bear is brown
	Cat is black
	Elephant is gray
	An animal is dark if it is black
	An animal is dark if it is brown
Write a query to find which animal is dark and big.
"""
#q2
from pyDatalog import pyDatalog
pyDatalog.create_terms('X,Y,Z,bear,elephant,cat,small,big,brown,black,gray,dark')
+big('elephant')
+big('bear')
+small('cat')
+black('cat')
+brown('bear')
+gray('elephant')
dark(X)<=black(X) or brown(X)
print(big(X),dark(X))
