"""3. The following are the marks scored by 5 students.
Student Name Mark
Ram 90
Raju 45
Priya 85
Carol 70
Shyam 80
Enter the above data using pyDatalog. Write queries for the following:
a. Print Student name and mark of all students.
b. Who has scored 80 marks?
c. What mark has been scored by Priya?
d. Write a rule ‘passm’ denoting that pass mark is greater than 50. Use the rule to print all students who failed.
e. Write rules for finding grade letters for a marks and use the rule to find the grade letter of a given mark.
"""
#Q3
from pyDatalog import pyDatalog
pyDatalog.create_terms('X,Y,Z,student,marks,passm,grades')
+student('Ram')
+student('Raju')
+student('Priya')
+student('Carol')
+student('Shyam')
+marks('90','Ram')
+marks('45','Raju')
+marks('85','Priya')
+marks('70','Carol')
+marks('80','Shyam')
+grades('Ram','O')
+grades('Priya','A')
+grades('Shyam','A')
+grades('Carol','B')
+grades('Raju','E')
print(marks(X,Y))
print(marks('80',X))
print(marks(X,'Priya'))
passm(X)<=grades(X,'E')
print(passm(X))
