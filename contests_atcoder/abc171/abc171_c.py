n = int(input())

sna = ""

while n:
    n, x = divmod(n, 26)
    if x == 0: x = 26; n -= 1
    sna += chr(ord("a") + x - 1)

print(sna[::-1])