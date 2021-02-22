from itertools import accumulate
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = sum(a)
if s < sum(b):
    print(-1)
else:
    count = 0
    need = 0
    supp = []
    for x, y in zip(a, b):
        if x < y:
            count += 1
            need += y - x
        else:
            supp.append(x - y)
    if need > sum(supp):
        print(-1)
    else:
        supp = [0] + list(accumulate(sorted(supp, reverse=True)))
        for i, x in enumerate(supp):
            if x >= need:
                count += i
                break
        print(count)