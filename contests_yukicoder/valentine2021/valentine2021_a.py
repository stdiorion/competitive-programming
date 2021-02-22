n, x = map(int, input().split())
c = list(map(int, input().split()))
if min(c) <= x <= max(c):
    print("Yes")
else:
    print("No")