n,x,*A=map(int,open(0).read().split())
o=[]
r=range
for k in r(1,n+1):
 d=[n*[-1e20]for _ in[n]*-~n];d[0][0]=0
 for a in A:
  for i in r(k,0,-1):
   for j in r(k):d[i][j]=max(d[i][j],d[i-1][(j-a)%k]+a)
 o+=[(x-d[k][x%k])//k]
print(min(o))