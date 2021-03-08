x = int(input())
now = 0
for i in range(360):
    now += x
    if now % 360 == 0:
        print(i + 1)
        exit()