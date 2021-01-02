n = int(input())

cnt = n

for i in range(1, n + 1):
    for dig in str(i) + format(i, 'o'):
        if dig == "7":
            cnt -= 1
            break

print(cnt)
