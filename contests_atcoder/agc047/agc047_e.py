op = []

def lt(i, j, dst):
    global op
    op.append(" ".join(list(map(str, ["<", i, j, dst]))))

def ad(i, j, dst):
    global op
    op.append(" ".join(list(map(str, ["+", i, j, dst]))))

n = 100

# Pointers
A = 0
B = 1
ans = 2
Acnt = 3
Acnt_tmp = 4
zero = 5
Bcnt = 6
Bcnt_tmp = 7
one = 8
oneA = 9
oneB = 10
and_cnt_tmp = 11

lt(zero, A, oneA)
lt(zero, B, oneB)
ad(oneA, oneB, one)
lt(zero, one, one)
for i in range(10):
    ad(zero, zero, Acnt)  # set Acnt to 0
    for _ in range(10):
        lt(Acnt, A, Acnt_tmp)
        lt(Bcnt, B, Bcnt_tmp)
        # and_cnt_tmp = Acnt_tmp and Bcnt_tmp = not (not Acnt_tmp or not Bcnt_tmp)
        ad(Acnt_tmp, Bcnt_tmp, and_cnt_tmp)
        lt(one, and_cnt_tmp, and_cnt_tmp)
        ad(Acnt, and_cnt_tmp, Acnt)
    
    lt(Bcnt, B, Bcnt_tmp)
    ad(Bcnt, Bcnt_tmp, Bcnt)

    ad(ans, Acnt, ans)

print(len(op))
print(*op, sep="\n")