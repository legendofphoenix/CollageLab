file=open(r"Desktop/CDEx1.c")

keywords=['int','float','string','include','stdio.h','char','break','if','else','switch','return','void','while','struct','for']

operators=['+','-','%','*','=','/','^','<','<']

specialSymbols={"(",")","{","}",";","&","#","$","\n",'"',","}

spec=["%d","%f","%c","%s"]
io=['scanf','printf','cin','cout']
num="012345678910"
iden=[]
n=[]
k=[]
o=[]
l=[]
dl=[]
F=[]

for lines in file:
    words=lines.split(" ")
    for i in range(len(words)):
        if words[i] in keywords:
            k.append(words[i])
        elif words[i] in io:
            l.append(words[i])
        elif words[i] in operators:
            o.append(words[i])
        elif words[i] in specialSymbols:
            dl.append(words[i])
        elif words[i] in spec:
           F.append(words[i])
        elif words[i] in num:
           n.append(words[i])
        else:
           iden.append(words[i])

print("Keywords are: ")
print(set(k))
print("input/output are: ")
print(set(l))
print("Operators are: ")
print(set(o))
print("Special Symbols are: ")
print(set(dl))
print("Identifiers are: " )
print(set(iden))
print("Format Specifier are:")
print(set(F))
print("Numbers are:")
print(set(n))
