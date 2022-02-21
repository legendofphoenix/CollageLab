#Question 3

import sqlite3
conn=sqlite3.connect('course')
curs=conn.cursor()
curs.execute('drop table product')
t1="create table product (ID int(5) , Prod_name varchar(20) , Suppliers_id int(10) , Unit_price int(10),\
Package varchar(20) , Order_id int(10) ,PRIMARY KEY(ID))"
curs.execute(t1)
rowst1 =[[2,"Shirt",5,50,"prime",6],[3,"shoes",8,60,"normal",7],[6,"pants",8,90,"prime",9]]
curs.executemany("insert into product values(?,?,?,?,?,?)",rowst1)
conn.commit()
curs.execute('drop table OrderItem')
t2="create table OrderItem (ID INT(5),Order_id int(10), Prod_id int(10),Unit_price REAL,Quantity int(10),\
FOREIGN KEY(Prod_id) REFERENCES product(Prod_id))"
curs.execute(t2)
curs.executemany("INSERT INTO OrderItem VALUES(?,?,?,?,?)",[(1,5,2,20,8),(2,7,3,30,6),(3,3,6,28.90,5)])
print("\n Part 1")
p1=curs.execute('select Prod_id,Quantity from OrderItem ')
for r in p1:
    print(r)
print("\n Part 2")
p2=curs.execute("select Unit_price,Suppliers_id FROM product ORDER BY Unit_price") 
for r in p2:
    print(r)
print("\n Part 3")    
p3=curs.execute("select Prod_name,Order_id,Suppliers_id FROM product")
for r  in p3:
    print(r)
