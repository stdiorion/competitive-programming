h, w, m = map(int, input().split())

top = [h] * w
left = [w] * h

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if left[a] > b:
        left[a] = b
    if top[b] > a:
        top[b] = a

topmin = h
tmin = [h] * w

for i in range(w):
    if top[i] < topmin:
        topmin = top[i]
    tmin[i] = topmin


print(sum(top[:left[0]]) + sum(left[:top[0]]) - sum(tmin))