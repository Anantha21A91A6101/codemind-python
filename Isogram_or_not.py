n=input()
c=0
m=0
for i in n:
    c=0
    for j in n:
        if i in j:
            c=c+1
    if c==1:
        m=m+1
if m==len(n):
    print("True")
else:
    print("False")