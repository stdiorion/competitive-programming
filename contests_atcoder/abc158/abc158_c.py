a, b = map(int, input().split())
for i in range(1, 110000):
    if i * 8 // 100 == a and i // 10 == b:
        print(i)
        exit()
print(-1)