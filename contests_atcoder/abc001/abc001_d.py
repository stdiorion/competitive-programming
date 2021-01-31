from itertools import accumulate

n = int(input())
rawdata = [input() for _ in range(n)]

imos = [0] * (12 * 24 + 1)

for rd in rawdata:
    start_, end_ = rd.split("-")

    start = int(start_[:2]) * 60 + int(start_[2:])
    end = int(end_[:2]) * 60 + int(end_[2:])

    start = start // 5
    end = (end + 4) // 5

    imos[start] += 1
    imos[end] -= 1

raining = False
ans = []
status = ""

for i, k in enumerate(accumulate(imos)):
    if k > 0:
        if not raining:
            status = str(i * 5 // 60).zfill(2) + str(i * 5 % 60).zfill(2) + "-"
            raining = True
    else:
        if raining:
            ans.append(status + str(i * 5 // 60).zfill(2) + str(i * 5 % 60).zfill(2))
            raining = False

print(*ans, sep="\n")