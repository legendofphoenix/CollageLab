#Question 1

import sqlite3
conn = sqlite3.connect('recipesdb')
curs = conn.cursor()
curs.execute('drop table recipes')
cmd="create table recipes (id int(11) ,name varcar(400), description text, category_id int(11),\
chef_id int (255), created datetime)"
conn.commit()
curs.execute(cmd)
curs.execute('insert into recipes values(1,"P5","good",111,000001,"20210309 23:53:12 PM")')
curs.execute('insert into recipes values(2,"P1","good",222,000002,"20210306 23:53:12 PM")')
curs.execute('insert into recipes values(2,"A2","good",333,000003,"20210301 23:53:12 PM")')
curs.execute('insert into recipes values(3,"B4","Chinese",333,000003,"20210301 23:53:12 PM")')

print("Before update")
curs.execute('select * from recipes')
for row in curs.fetchall():
    print(row)
print("\nAfter update")
curs.execute('update recipes set name="D3" where id = 2')
curs.execute('select * from recipes')
for row in curs.fetchall():
    print(row)
print("\n Part 1")
p2=curs.execute('select id, name from recipes where description="Chinese"')
for r in p2:
    print(r)
print("\n Part 3")
p3=curs.execute('select * from recipes where name like "P%"')
for row in p3:
    print(row)
