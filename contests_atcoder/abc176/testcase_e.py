
H = 300000
W = 300000
m = 520
M = m * m

with open("test_e_line.txt", "w") as f:
    print(H, W, M, file=f)
    for i in reversed(range(M)):
        print(1, i + 1, file=f)