def Swap(x,y):
    x = x + y
    y = x - y
    x = x - y
    print("After Swapping: first =", x, " second =", y)
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
Swap(n1,n2)
