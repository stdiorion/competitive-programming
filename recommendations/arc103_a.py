from collections import Counter

n = int(input())
v = list(map(int, input().split()))

count_e = Counter(v[0::2]).most_common(2)
count_o = Counter(v[1::2]).most_common(2)

if count_e[0][0] != count_o[0][0]:
    print(n - count_e[0][1] - count_o[0][1])
elif len(count_e) == len(count_o) == 1:
    print(n // 2)
elif len(count_e) == 1:
    print(n // 2 - count_o[1][1])
elif len(count_o) == 1:
    print(n // 2 - count_e[1][1])
else:
    print(n - max(count_e[0][1] + count_o[1][1], count_e[1][1] + count_o[0][1]))