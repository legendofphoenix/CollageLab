#Question 1 set9 week 1
list1=[]
list2=[]
print("On challenge day")
for i in range(0,3):
    w=int(input())
    list1.append(w)
print("One month later")
for i in range(0,3):
    w=int(input())
    list2.append(w)
max=0
for i in range(0,3):
    if(list1[i]-list2[i]>max):
        max = list1[i]-list2[i]
        j=i+1
print("Winner is: friend",j)
