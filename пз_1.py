def F(a,b,c,x):
    if a!=0 and x>0:
        return x/a
    if a<0:
        return -x*a-b
    else:
        return b*x+c

for x in range(-2, 5, 1):
    print(F(2, 3, 1, -2))
