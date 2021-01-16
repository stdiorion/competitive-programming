# 平方分割

n, q = map(int, input().split())
a = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(q)]

def xor_list(l):
    if not len(l): return 0
    ret = l[0]
    for k in l[1:]:
        ret ^= k
    return ret

def xor_range(lower, upper):
    i_left = lower // sqrtn + 1
    i_right = upper // sqrtn
    if i_right - i_left > 0:
        lst = a[lower:i_left * sqrtn] + a_rapid[i_left:i_right] + a[i_right * sqrtn: upper + 1]
    else:
        lst = a[lower:upper + 1]
    return xor_list(lst)

sqrtn = int(n ** 0.5) + 1

a_rapid = [xor_list(a[i * sqrtn: (i + 1) * sqrtn]) for i in range(sqrtn)]

for query in queries:
    x = query[1] - 1
    y = query[2]
    if query[0] == 1:
        a[x] ^= y
        a_rapid[x // sqrtn] ^= y
    else:
        print(xor_range(x, y - 1))