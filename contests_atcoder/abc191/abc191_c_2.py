h,w=map(int,input().split())
s=[input()for _ in[0]*h]
print(sum((s[i][j:j+2]+s[i+1][j:j+2]).count("#")%2 for j in range(w-1)for i in range(h-1)))