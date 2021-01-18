n = input()
if int(n) <= int(n[0] * len(n)):
    print(int(n[0] * len(n)))
else:
    print(int(str(int(n[0])+1) * len(n)))