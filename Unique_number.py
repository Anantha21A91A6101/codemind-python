n=int(input())
k=list()
c=0
while n>0:
    r=n%10
    k.append(r)
    n=n//10
for i in k:
    if k.count(i)>1:
        c=c+1
if c==0:
    print("Unique Number")
else:
    print("Not Unique Number");