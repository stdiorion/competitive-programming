a, b = map(int, input().split())

def xor_sum(x):
    if x % 4 == 0:
        return x
    if x % 4 == 1:
        return 1
    if x % 4 == 2:
        return x + 1
    if x % 4 == 3:
        return 0

print(xor_sum(a - 1) ^ xor_sum(b))