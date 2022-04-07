non_terminals = []
pn=[]
pt1=[]
pt2=[]
pt3=[]
print("Enter the non terminals :")
non_terminals.append(input())
print("1st")
pn.append(input())
print("2nd")
pt1.append(input())
print("3rd")
pt2.append(input())
print("4th")
pt3.append(input())

lo =[]
lo.append(pn)
lo.append(pt1)
lo.append(pt2)
lo.append(pt3)
lo
l= list(zip( lo[0],lo[1],lo[2],lo[3]))
gram = dict(zip(non_terminals,l))
"""gram = {
    "S":["S*S","S+S","i"]
}"""
starting_terminal = "S"
print("Input String:- ")
inp = input();

stack = "$"
print(f'{"Stack": <15}'+"|"+f'{"Input Buffer": <15}'+"|"+f'Parsing Action')
print(f'{"-":-<50}')

while True:
    action = True
    i = 0
    while i<len(gram[starting_terminal]):
        if gram[starting_terminal][i] in stack:
            stack = stack.replace(gram[starting_terminal][i],starting_terminal)
            print(f'{stack: <15}'+"|"+f'{inp: <15}'+"|"+f'Reduce S->{gram[starting_terminal][i]}')
            i=-1
            action = False
        i+=1
    if len(inp)>1:
        stack+=inp[0]
        inp=inp[1:]
        print(f'{stack: <15}'+"|"+f'{inp: <15}'+"|"+f'Shift')
        action = False

    if inp == "$" and stack == ("$"+starting_terminal):
        print(f'{stack: <15}'+"|"+f'{inp: <15}'+"|"+f'Accepted')
        break

    if action:
        print(f'{stack: <15}'+"|"+f'{inp: <15}'+"|"+f'Rejected')
        break
