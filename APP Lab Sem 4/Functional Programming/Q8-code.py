""" 8. Filter
The marks scored by a class of students in 5 different subjects are stored in a list of lists. Using the filter function, write a program to find the students 
who failed in one or more subjects.
"""

marks = [[88, 77, 66, 77, 99],[56, 78, 31, 35, 54],[53, 71, 64, 56, 14]]
def fail(marks):
    for i in marks:
        if i < 40:
            return True
result = filter(fail, marks)
res = list(result)
for i in range(0, len(marks)):
    if marks[i] in res:
        print("Student #{} failed in at least one subject.".format(i+1))
