p,r,t=map(float,input().split())
k=((1+r/100)**(t))
s=p*k
d="{:.2f}".format(s)
print(d)