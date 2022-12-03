n=input()
k=0
m=0
for i in range(0,len(n)):
    if n[i] in 'aeiou':
        k=k+1
        if k==1:
            print("V",end="")
            m=0
    else:
        m=m+1
        if m==1:
            print("C",end="")
            k=0