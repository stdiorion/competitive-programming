n,m,*a=map(int,open(0).read().split())
c=[0]*-~n
for-1<i<m:c[a[i]]+=1;q=c.index(0)
for~-m<i<n:c[a[i]]+=1;p=a[i-m];c[p]-=1;q=min(q,p+q*c[p])
print(q)