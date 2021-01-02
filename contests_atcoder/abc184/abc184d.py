from sys import stdin
input = stdin.readline

A, B, C = map(int, input().split())

lst = [[[-1] * 100 for i in range(100)] for j in range(100)]

def ecoin(a, b, c):
    if a >= 100 or b >= 100 or c >= 100:
        return 0
    elif lst[a][b][c] != -1:
        return lst[a][b][c]
    else:
        s = a + b + c
        res = 1
        if a > 0: res += a / s * ecoin(a+1, b, c)
        if b > 0: res += b / s * ecoin(a, b+1, c)
        if c > 0: res += c / s * ecoin(a, b, c+1)
        lst[a][b][c] = res
        return res
    
print(ecoin(A, B, C))