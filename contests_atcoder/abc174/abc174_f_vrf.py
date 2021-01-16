from random import randint

for _ in range(10000):
    n, Q = randint(1, 10), randint(1, 10)
    a = [randint(1, n) for _ in range(n)]
    queries = [[randint(1, n // 2), randint(n // 2, n)] for _ in range(Q)]

    
    def xor_range(lower, upper):
        i_left = lower // sqrtn + 1
        i_right = upper // sqrtn
        if i_right - i_left > 0:
            lst = set(a[lower:i_left * sqrtn]) | set(a[i_right * sqrtn: upper + 1])
            for i in range(i_left, i_right):
                lst |= a_rapid[i]
        else:
            lst = set(a[lower:upper + 1])
        return len(lst)

    sqrtn = int(n ** 0.5) + 1

    a_rapid = [set(a[i * sqrtn: (i + 1) * sqrtn]) for i in range(sqrtn)]

    for q in queries:
        x = q[0] - 1
        y = q[1] - 1
        print(xor_range(x, y))