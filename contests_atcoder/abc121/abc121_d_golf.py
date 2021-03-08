#a,b=map(int,input().split())
X=lambda x:(x,1,x+1,0)[x%4]
#print(X(a-1)^X(b));a,b=map(int,input().split())
print(eval("X("+input().replace(" ","-1)^X(")+")"))