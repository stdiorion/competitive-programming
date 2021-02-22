n,k,*x=map(int,open(0).read().split())
print(2*sum(min(v,k-v)for v in x))