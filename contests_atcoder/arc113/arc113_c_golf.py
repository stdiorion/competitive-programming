s=input()[::-1]
A=i=0
m={}
while~-len(s)>i:
 m.setdefault(t:=s[i],0);m[t]+=1;i+=1
 if t==s[i]:A+=i-m[t];m={t:i}
print(A)