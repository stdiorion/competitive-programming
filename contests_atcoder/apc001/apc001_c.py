n = int(input())

status = [-1] * (n + 1)

def send(q):
    print(q)
    s = input()
    if s == "Vacant":
        exit()
    else:
        return int(s == "Male")

lo = 0
hi = n
mid = (hi - lo) // 2

status[0] = status[n] = send(0)

for i in range(19):
    status[mid] = send(mid)
    if status[lo] ^ status[mid] == (mid - lo) & 1:
        lo = mid
    else:
        hi = mid
    mid = (hi - lo) // 2 + lo