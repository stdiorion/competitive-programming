import sys
input = sys.stdin.readline

t = int(input())
S = [input() for _ in range(t)]

for s in S:
    print(s.count("b"))