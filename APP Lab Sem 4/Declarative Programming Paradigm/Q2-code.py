#Question 2

import sqlite3
conn=sqlite3.connect('lab5')
curs=conn.cursor()
curs.execute('drop table movie')
cmd="create table movie(Movie_ID int(200) ,Movie_name varchar(100) , Genre varchar(100) , Language varchar(50)\
, Rating int(10))"
curs.execute(cmd)
curs.execute('insert into movie values(1,"Ironman","SiFi","English",5)')
curs.execute('insert into movie values(2,"Avengers","SiFi","English",5)')
curs.execute('insert into movie values(10,"Spiderman","SiFi","English",5)')
curs.execute('insert into movie values(102,"MadMax","SiFi","English",2)')
curs.execute('select * from movie')
for row in curs.fetchall():
    print(row)
print("\n Part 1")
curs.execute('update movie set Rating=Rating+(Rating*0.10)')
curs.execute('select * from movie')
for row in curs.fetchall():
    print(row)
print("\n Part 2")
p2=curs.execute('select * from movie where Movie_ID=102')
for r in p2:
    print(r)
print("\n Part 3")
p3=curs.execute('select * from movie where Rating>3')
for r in p3:
    print(r)
