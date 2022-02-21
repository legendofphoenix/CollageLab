#Question 4

import sqlite3
conn=sqlite3.connect("lab5")
curs=conn.cursor()
curs.execute("DROP table job")
table="create table job (job_id int(10) PRIMARY KEY, job_title varchar(20) , min_salary int(10) , max_salary int(10))"
curs.execute(table)
rows=[[1,'Manager',1000,50000],[2,'Assisistent',1000,30000]]
curs.executemany("insert into job values(?,?,?,?)",rows)
a=curs.execute("select * from job")
for r in a:
    print(r)
curs.executemany("insert into job values(?,?,?,?)",rows)
