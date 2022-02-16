l=[0]
f1 = 0
f2 = 1
for x in range(1, 11):
    l.append(f2)
    next = f1 + f2
    f1 = f2
    f2 = next
print(l)
odd = filter(lambda a: True if a%2!=0 else False , l)
print("Odd :", list(odd))
even = filter(lambda a: True if a%2==0 else False , l)
print("Even :",list(even))
