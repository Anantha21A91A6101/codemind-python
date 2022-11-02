def prime(n):
    if n<2:
        return 1
    for i in range(2,n):
        if n%i==0:
            return 1
    return 0
n=int(input())
y=0
for i in range(1,n):
    if(prime(i)==0):
        for j in range(1,i):
            if(prime(j)==0 and i*j==n):
                y=1
                print(j,i,end=" ")
    if y==1:
        break
if y==0:
    print("-1")