from collections import*
I=lambda:[*map(int,input().split())]
n,m=I()
g=[[]for _ in[n]*-~n]
for _ in[m]*m:a,b=I();g[a]+=[b];g[b]+=[a]
k=I()[0]
c=I()
F=1<<k
G=[k*[F]for-1<_<k]
for-1<i<k:
 D=[F]*-~n;D[c[i]]=0;q=deque([c[i]])
 while q:
  v=q.popleft()
  for t in g[v]:
   if D[t]==F:D[t]=D[v]+1;q+=[t]
 G[i]=[D[c[j]]for-1<j<k]
p=[k*[F]for-1<_<F]
for-1<i<k:p[1<<i][i]=1
for-1<b<F:
 for-1<v<k:
  if b>>v&1:
   for-1<u<k:p[b|1<<u][u]=min(p[b|1<<u][u],p[b][v]+G[v][u])
a=min(p[-1])
print([-1,a][a<F])