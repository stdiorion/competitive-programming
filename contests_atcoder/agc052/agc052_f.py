from random import shuffle, randint, sample, choice
def verify(ans, s1, s2, s3, n):
    s1 *= 2
    s2 *= 2
    s3 *= 2
    i1 = i2 = i3 = 0
    for l1, l2, l3 in zip(s1, s2, s3):
        if i1 < 2 * n + 1 and ans[i1] == l1:
            i1 += 1
        if i2 < 2 * n + 1 and ans[i2] == l2:
            i2 += 1
        if i3 < 2 * n + 1 and ans[i3] == l3:
            i3 += 1

    return i1 == i2 == i3 == 2 * n + 1

for _ in range(1000):
    n = randint(1, 5000)
    s1 = s2 = s3 = "01" * n
    s1 = list(s1)
    s2 = list(s2)
    s3 = list(s3)
    shuffle(s1)
    shuffle(s2)
    shuffle(s3)
    s1 = "".join(s1)
    s2 = "".join(s2)
    s3 = "".join(s3)

    ans = ("0" * n + "1" + "0" * n)
    if not verify(ans, s1, s2, s3, n):
        ans = ("1" * n + "0" + "1" * n)
    if not verify(ans, s1, s2, s3, n):
        ans1 = "1" + "0" * (n - 1)
        ans = ans1 + "0" + ans1
        if not verify(ans, s1, s2, s3, n):
            ans1 = "1" + "0" * (n - 1)
            ans = ans1 + "1" + ans1
            if not verify(ans, s1, s2, s3, n):
                ans1 = "1" * (n - 1) + "0"
                ans = ans1 + "0" + ans1
                if not verify(ans, s1, s2, s3, n):
                    ans1 = "1" * (n - 1) + "0"
                    ans = ans1 + "1" + ans1
                    if not verify(ans, s1, s2, s3, n):
                        ans = s1 + s1[0]
                        if not verify(ans, s1, s2, s3, n):
                            ans = s2 + s2[0]
                            if not verify(ans, s1, s2, s3, n):
                                ans = s3 + s3[0]
                                if not verify(ans, s1, s2, s3, n):
                                    ans1 = "1" * (n - 2) + "0" + "1"
                                    ans = ans1 + "0" + ans1
                                    if not verify(ans, s1, s2, s3, n):
                                        ans = ""
    if ans == "":
        ans1 = "0" + "1" * (n - 1)
        ans = ans1 + "1" + ans1
        if not verify(ans, s1, s2, s3, n):
            ans1 = "0" + "1" * (n - 1)
            ans = ans1 + "0" + ans1
            if not verify(ans, s1, s2, s3, n):
                ans1 = "0" * (n - 1) + "1"
                ans = ans1 + "1" + ans1
                if not verify(ans, s1, s2, s3, n):
                    ans1 = "0" * (n - 1) + "1"
                    ans = ans1 + "0" + ans1
                    while not verify(ans, s1, s2, s3, n):
                        ans = "".join(s1[i] for i in sorted(sample(range(2 * n), k=n)))
                        ans = ans + choice("01") + ans

    s1 *= 2
    s2 *= 2
    s3 *= 2
    i1 = i2 = i3 = 0
    for l1, l2, l3 in zip(s1, s2, s3):
        if i1 < 2 * n + 1 and ans[i1] == l1:
            i1 += 1
        if i2 < 2 * n + 1 and ans[i2] == l2:
            i2 += 1
        if i3 < 2 * n + 1 and ans[i3] == l3:
            i3 += 1

    if i1 == i2 == i3 == 2 * n + 1:
        pass
    else:
        print(n)
        print(s1)
        print(s2)
        print(s3)
        print(ans)
        print(i1,i2,i3)