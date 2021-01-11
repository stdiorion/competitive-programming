from bisect import bisect_left, bisect_right
from collections import deque, Counter
from itertools import combinations, permutations
from math import gcd, sin, cos, tan, degrees, radians, sqrt
import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 9 + 7
INF = float("inf")

s = input()
t = input()

def findall(st, q):
    idx = -1
    ret = []
    while True:
        idx = st.find(q, idx + 1)
        if idx == -1:
            break
        else:
            ret.append(idx)
    return ret

char_pos = dict()

for i in range(ord("a"), ord("a") + 26):
    char_pos[chr(i)] = findall(s, chr(i))

cursor = -1
loop_count = 0

for char in t:
    if not len(char_pos[char]):
        print(-1)
        exit()
    
    new_cursor_idx = bisect_right(char_pos[char], cursor)

    if new_cursor_idx == len(char_pos[char]):
        new_cursor = char_pos[char][0]
        loop_count += 1
    else:
        new_cursor = char_pos[char][new_cursor_idx]
    
    cursor = new_cursor

ans = loop_count * len(s) + cursor + 1

print(ans)