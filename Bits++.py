t=int(input())
c=0
while t>0:
    x=(input())
    if x[1]=='+':
        c=c+1
    else:
        c=c-1
    t=t-1
print(c)