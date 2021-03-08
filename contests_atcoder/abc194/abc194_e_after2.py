N,M,*A=map(int,open(i:=0).read().split())
N+=1
L=[-1]*N
T=[0]*N
for v in A:T[v]|=i-L[v]>M;i+=1;L[v]=i
print(min(v for-1<v<N if T[v]or N-M>L[v]))