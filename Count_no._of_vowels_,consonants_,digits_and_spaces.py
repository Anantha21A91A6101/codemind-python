a=input()
c=0
d=0
k=0
m=0
for i in range(0,len(a)):
    if a[i] in'aeiouAEIOU':
        c=c+1
    elif a[i] in ' ':
        k=k+1
    elif a[i]>='0' and a[i]<='9':
        m=m+1
    else:
        d=d+1
print('Vowels:',c)
print('Consonants:',d)
print('Digits:',m)
print('White spaces:',k)