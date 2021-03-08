n,*a=map(int,open(0).read().split())
print(sum(n*x**2for x in a)-sum(a)**2)