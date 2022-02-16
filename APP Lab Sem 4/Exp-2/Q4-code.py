def Celsius(F):
    C = ((5.0/9.0)*(F - 32))
    return C
f = [98.5, 101,102,203,104]
t = (map(Celsius, f))
c = list(t)
print(c)
