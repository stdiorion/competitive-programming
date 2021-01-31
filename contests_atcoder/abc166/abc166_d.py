x = int(input())

for i in range(1000):
    for j in range(1000):
        I = i ** 5
        J = j ** 5
        if I - J == x:
            print(i, j)
            exit()
        if I + J == x:
            print(i, -j)
            exit()
        if -I - J == x:
            print(-i, j)
            exit()
        if -I + J == x:
            print(-i, -j)
            exit()