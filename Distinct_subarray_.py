n=int(input())
m=int(input())
s=0
for i in range(n,m+1):
    c=0
    for j in range(i,m+1):
        c=c+j
        if c%2!=0:
            s=s+1
print(s)            