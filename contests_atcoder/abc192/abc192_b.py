s = input()
lo = s[::2]
up = s[1::2]

for x in lo:
    if x.isupper():
        print("No")
        exit()

for x in up:
    if x.islower():
        print("No")
        exit()

print("Yes")