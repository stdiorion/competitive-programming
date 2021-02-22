from random import randint
import random
import string
from collections import deque

def solve(s, Q, queries):
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
        ans = reversed(ans)

    return "".join(ans)

def ans(s, Q, queries):
    for q in queries:
        if q[0] == "1":
            s = s[::-1]
        else:
            if q[1] == "2":
                s = s + q[2]
            else:
                s = q[2] + s
    return s


for _ in range(100):
    s = "".join(random.choices(string.ascii_lowercase, k=randint(1, 3)))
    Q = randint(1, 10)
    queries = []
    for _ in range(Q):
        if randint(0, 1):
            queries.append("1")
        else:
            q = "2 " + str(randint(1, 2)) + " " + random.choice(string.ascii_lowercase)
            queries.append(q)
    
    ans1 = solve(s, Q, queries)
    ans2 = ans(s, Q, queries)

    if ans1 != ans2:
        print(s)
        print(Q)
        print(*queries, sep="\n")
        print("OMG", ans1, ans2)