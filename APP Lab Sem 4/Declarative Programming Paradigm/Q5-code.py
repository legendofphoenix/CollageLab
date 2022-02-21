#Question 5

import sqlite3
conn=sqlite3.connect("lab5")
curs=conn.cursor()
curs.execute("drop table job_history")
curs.execute("drop table job")
t1="create table job (job_id int(10) PRIMARY KEY, job_title varchar(20) , min_salary int(10) , max_salary int(10))"
curs.execute(t1)
curs.executemany("INSERT INTO job VALUES(?,?,?,?)",[[1,'Manager',1000,50000],[2,'Assisistent',1000,30000]])
conn.commit()
t2="create table job_history (employee_id int(5) PRIMARY KEY,start_date varcar(5),end_date varcar(5),job_id int(5),\
FOREIGN KEY('job_id') references job('job_id'))"
curs.execute(t2)
curs.executemany("INSERT INTO job_history VALUES(?,?,?,?)"\
                 ,[ (1,'2 feb 2015','6 june 2018',1),(2,'8 dec 2013','3 jan 2021',2)])
conn.commit()
p=curs.execute("SELECT * FROM job_history")
for r in p:
    print(r)
