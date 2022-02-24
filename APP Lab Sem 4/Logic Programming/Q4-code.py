""" 4. Solve the set of queries in the previous question using imperative programming paradigm in Python. Store the data in a dictionary."""
#Q4
marks={90:'Ram',85:'Priya',80:'Shyam',70:'Carol',45:'Raju'}
for i in marks:
    print(i,marks[i])
print(marks[80])
for i in marks:
    if marks[i]=='priya':
        print(i)
for i in marks:
    if i<50:
        print(marks[i])
for i in marks:
    if i>=90:
        print(marks[i],'O')
    elif i<90 and i>=80:
        print(marks[i],'A')
    elif i<80 and i>=70:
        print(marks[i],'B')
    elif i<70 and i>=60:
        print(marks[i],'C')
    elif i<60 and i>=50:
        print(marks[i],'D')
    else:
        print(marks[i],'E')
