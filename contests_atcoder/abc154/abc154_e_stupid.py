n = int(input())
k = int(input())

count = 0
prev = 0

for i in range(1, n + 1):
    if i == 300000:
        print(count - prev)
        prev = count
    if i == 100000:
        print(count - prev)
        prev = count
    I = str(i)
    if len(I) - I.count("0") == k:
        count += 1
        #if i >= 300000: print(i)

print(count - prev)
print(count)