n,m,c,*K=map(int,open(0).read().split())
print(sum(-c<sum(K[j]*K[-~i*m+j]for j in range(m))for i in range(n)))