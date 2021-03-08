from operator import itemgetter
n = int(input())
w = [list(map(int, input().split())) + [i] for i in range(n)]

a = sorted(w, key=itemgetter(0, 2))
b = sorted(w, key=itemgetter(1, 2))

if a[0][2] != b[0][2]:
    print(max(a[0][0], b[0][1]))
else:
    print(min(a[0][0] + b[0][1], max(a[0][0], b[1][1]), max(a[1][0], b[0][1])))

exit()

n,*w=map(int,open(0).read().split())
print(min((max(w[k//n*2],v:=w[(b:=k%n*2)+1]),w[b]+v)[b/2==k//n]for k in range(n*n)))

exit()

n,*w=map(int,open(0).read().split())
print(min(max(w[a*2],w[b+1])if(b:=k%n*2)/2-(a:=k//n)else w[b+1]+w[b]for k in range(n*n)))


exit()

n=int(input())
w=[list(map(int,input().split()))for _ in[n]*n]
print(min(max(w[a][0],w[b][1])if a-b else w[a][0]+w[b][1]for a in range(n)for b in range(n)))