k = int(input())
s = [int(x) for x in input()[:-1]]
t = [int(x) for x in input()[:-1]]

remain = [k] * 10
remain[0] = 0

for x in s + t:
    remain[x] -= 1

def point(hand):
    c = [0] * 10
    for x in hand:
        c[x] += 1
    res = 0
    for i in range(1, 10):
        res += i * 10 ** c[i]
    return res

win = 0
lose = 0

for i in range(1, 10):
    for j in range(1, 10):
        if i == j:
            pat = remain[i] * (remain[i] - 1)
        else:
            pat = remain[i] * remain[j]
        if point(s + [i]) > point(t + [j]):
            win += pat
        else:
            lose += pat

print(win / (win + lose))