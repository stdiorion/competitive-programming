n = int(input())
def make(m, l):
    if len(m) == n:
        print(m)
        return 0
    for next in range(97, l):
        make(m + chr(next), l)
    make(m + chr(l), l + 1)

make("", 97)