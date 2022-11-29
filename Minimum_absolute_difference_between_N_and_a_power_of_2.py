n=int(input())
from math import floor,log2
l=pow(2,floor(log2(n)))
r=l*2
l=n-l
r=r-n
k=min(l,r)
print(k)