n,m,k=map(int,input().split())
w=pow
p=998244353
print(sum((w(-~i,n,p)-w(i,n,p))*w(k-i,m,p)for i in range(k))%p if~-min(n,m)else w(k,~-n+m,p))