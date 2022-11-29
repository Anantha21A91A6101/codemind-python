def prime(i):
    c=0
    if i<2:
        return False
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            return False
    return True

n=int(input())
m=int(input())
s=0
for i in range(n,m+1,1):
    if(prime(i)):
        s=s+1
print(s)