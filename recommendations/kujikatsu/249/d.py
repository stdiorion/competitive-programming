from heapq import heappop, heappush
s = input()
k = int(input())

first = sorted(s)[0]

if k == 1:
    print(first)

q = []

for i, x in enumerate(s):
    heappush(q, (x, i))

counter = 2
done = set()
while q:
    now, idx = heappop(q)
    
    
    if counter == k:
        print(now)
        exit()
    if now not in done:
        done.add(now)
        counter += 1

    if idx < len(s) - 1:
        idx += 1
        heappush(q, (now + s[idx], idx))
