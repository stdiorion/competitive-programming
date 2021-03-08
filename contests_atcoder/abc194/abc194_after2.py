n,m,*a=map(int,open(0).read().split())
c=[0]*-~n
for x in a[:m]:c[x]+=1
q=c.index(0)
for p,x in zip(a,a[m:]):c[p]-=1;c[x]+=1;q=min(q,p+q*c[p])
print(q)