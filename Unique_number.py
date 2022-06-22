n=int(input())
l=list()
m=0
while n>0:
    r=n%10
    l.append(r)
    n=n//10
for i in l:
    if l.count(i)>1:
        m=m+1
if m==0:
    print('Unique Number')
else:
    print('Not Unique Number')