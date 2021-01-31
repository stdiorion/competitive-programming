from heapq import heappop, heappush
from collections import defaultdict

n, Q = map(int, input().split())
infants = [tuple(map(int, input().split())) for _ in range(n)]
queries = [tuple(map(int, input().split())) for _ in range(Q)]

rating = [x[0] for x in infants]
belong = [x[1] for x in infants]

kg = defaultdict(list)
bests = []

for i, x in enumerate(infants):
    heappush(kg[x[1]], (-x[0], i))

for key in kg:
    heappush(bests, (-kg[key][0][0], kg[key][0][1], key))

for c, d in queries:
    c -= 1
    if kg[belong[c]][0][1] == c:
        heappop(kg[belong[c]])
        while len(kg[belong[c]]) and belong[kg[belong[c]][0][1]] != belong[c]:
            heappop(kg[belong[c]])
        if len(kg[belong[c]]):
            heappush(bests, (-kg[belong[c]][0][0], kg[belong[c]][0][1], belong[c]))
    belong[c] = d
    heappush(kg[d], (-rating[c], c))
    heappush(bests, (rating[c], c, d))

    while belong[bests[0][1]] != bests[0][2] or kg[bests[0][2]][0][1] != bests[0][1]:
        keys = []
        for i in range(3):
            if len(bests):
                keys.append(heappop(bests)[2])
        for key in keys:
            while len(kg[key]) and belong[kg[key][0][1]] != key:
                heappop(kg[key])
            if len(kg[key]):
                heappush(bests, (-kg[key][0][0], kg[key][0][1], key))
    
    print(bests[0][0])