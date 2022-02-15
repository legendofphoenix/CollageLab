no = int(input("Enter a number: "))
sum=0
temp=no
x=no
n=0
while (x != 0): 
        n = n + 1
        x = x // 10
while temp > 0:
    m = temp % 10
    sum += m**n 
    temp //= 10
if(no == sum):
    print(no,"is an Armstrong number")
else:
    print(no,"is not an Armstrong number")
