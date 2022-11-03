def prime(n):
    if n<2:
        return 0
    for i in range(2,n):
        if n%i==0:
            return 0;
    return 1;
n=int(input())
y=0
for i in range(1,n):
    if(prime(i)):
        for j in range(1,i):
            if(prime(j) and i*j==n):
                print(j,i,end=" ")
                y=1
                break
    if y==1:
        break
if y==0:
    print("-1")