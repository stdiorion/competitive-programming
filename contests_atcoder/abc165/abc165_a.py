k = int(input())
a, b = map(int, input().split())

for K in range(k, 1001, k):
    if a <= K <= b:
        print("OK")
        exit()

print("NG")