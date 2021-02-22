from collections import Counter, defaultdict
from bisect import bisect_left
n = int(input())
a = list(map(int, input().split()))
c = Counter(a)
choice = defaultdict(int)
choice_k = defaultdict(int)
for key in c:
    choice[key] = c[key] * (c[key] - 1) // 2 if c[key] > 0 else 0 
    choice_k[key] = (c[key] - 1) * (c[key] - 2) // 2 if c[key] > 1 else 0
choice_sf = [0]
choice_sb = [0]
keys = sorted(list(c.keys()))
for key in keys:
    choice_sf.append(choice_sf[-1] + choice[key])
for key in reversed(keys):
    choice_sb.append(choice_sb[-1] + choice[key])
choice_sb.reverse()
for x in a:
    idx = bisect_left(keys, x)
    print(choice_k[x] + choice_sf[idx] + choice_sb[idx + 1])