a,b,c=map(int,input().split())
print("YNeos"[4*a*b>=max(0,c-a-b)**2::2])