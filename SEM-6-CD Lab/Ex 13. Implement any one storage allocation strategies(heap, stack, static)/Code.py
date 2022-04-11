stack = []
 
# append() function to push element in the stack
print("Enter Number/Alphabets for the Stack to push : ")
for x in range(0,5):
    d=input()
    stack.append(d)
#stack.append('b')
 
print('\nInitial stack')
print(stack)
 
# pop() function to pop element from stack in LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
 
print('\nStack after elements are popped:')
print(stack)

