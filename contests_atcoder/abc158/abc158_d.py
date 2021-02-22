from collections import deque
s = input()
Q = int(input())
queries = [tuple(input().split()) for _ in range(Q)]

ans = deque()
ans.append(s)

reverse = 0

for q in queries:
    if q[0] == "1":
        reverse ^= 1
    else:
        if (q[1] == "2") ^ reverse:
            ans.append(q[2])
        else:
            ans.appendleft(q[2])

if reverse:
    ans = "".join(x[::-1] for x in reversed(ans))

print(*ans, sep="")