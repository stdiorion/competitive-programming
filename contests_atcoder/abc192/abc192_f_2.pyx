n,x,*A=map(int,open(0).read().split())
o=1e20
for 0<k<=n:
 d=[n*[-1e20]for _ in[n]*-~n];d[0][0]=0
 for a in A:
  for k>=i>0:
   for-1<j<k:
    d[i][j]=max(d[i][j],d[i-1][(j-a)%k]+a)
 o=min(o,(x-d[k][x%k])//k)
print(o)