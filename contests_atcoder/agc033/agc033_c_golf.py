from collections import*
n,*E=map(int,open(0).read().split())
g=[[]for _ in[n]*-~n]
for a,b in zip(E[::2],E[1::2]):g[a]+=[b];g[b]+=[a]
def b(s):
 d=deque([(s,1)]);Q=[1]*-~n
 while d:
  v,c=d.popleft();Q[v]=0
  for t in g[v]:d+=[(t,c+1)]*Q[t]
 return v,c
print("SFeicrosntd"[b(b(1)[0])[1]%3<2::2])