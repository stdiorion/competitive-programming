import re
exec(re.sub("`(.)",r"for \1 in ","""from collections import*
I=lambda:[*map(int,input().split())]
n,m=I()
g=[[]`_[n]*-~n]
`_[m]*m:a,b=I();g[a]+=[b];g[b]+=[a]
k=I()[0]
c=I()
F=1<<k
r,R=range(k),range(F)
G=[k*[F]`_r]
`ir:
 D=[F]*-~n;D[c[i]]=0;q=deque([c[i]])
 while q:
  v=q.popleft()
  `tg[v]:
   if k<D[t]:D[t]=D[v]+1;q+=[t]
 G[i]=[D[c[j]]`jr]
p=[k*[F]`_R]
`ir:p[1<<i][i]=1
`bR:
 `vr:
  if b&1<<v:
   `ur:p[b|1<<u][u]=min(p[b|1<<u][u],p[b][v]+G[v][u])
a=min(p[-1])
print([-1,a][a<F])"""))