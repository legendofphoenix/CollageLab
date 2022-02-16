l1=[1,2,3,4,5,6]
l2=[4,6,12,3,2,1]
result = list(map(lambda x, y: x + y, l1, l2))
print("Sum of list 1 and 2 :",list(result))
l3=[4,2,8,3,2,1]
result1 = map(lambda x, y: x * y,result,l3)
print("After multiplication with l3 :",list(result1))
