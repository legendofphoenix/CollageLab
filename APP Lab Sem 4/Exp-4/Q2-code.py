#Quetion 2 set 9 week 1
def bill(u):
    if(u<=100):
        return u*100
    if(u<=200):
        return ((100*0)+(u-100)*1)
    if(u<=300):
        return ((100*0)+(100*1)+(u-200)*2)
    if(u>300):
        return ((100*0)+(100*1)+(100*2)+(u-300)*2)
x=int(input("Previous reading: "))
y=int(input("Current reading: "))
units=y-x
print("Bill amount:",bill(units))
