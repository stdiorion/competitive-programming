from bisect import bisect_left, bisect_right
from collections import deque, Counter
from itertools import combinations, permutations
from math import gcd, sin, cos, tan, degrees, radians
import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 9 + 7
INF = float("inf")

n = int(input())
cards = [list(map(int, input().split())) for _ in range(n)]

card_count = [0] * 400001
chosen = set()

for card in cards:
    if card[0] == card[1]:
        if card[0] not in chosen:
            chosen.add(card[0])
    else:
        card_count[card[0]] += 1
        card_count[card[1]] += 1

cards_with_count = [[min(card_count[cards[i][0]], card_count[cards[i][1]])] + [max(card_count[cards[i][0]], card_count[cards[i][1]])] + cards[i] for i in range(n)]

cards_with_count.sort()

for card in cards_with_count:
    if card_count[card[3]] < card_count[card[2]]:
        if card[3] not in chosen:
            chosen.add(card[3])
        elif card[2] not in chosen:
            chosen.add(card[2])
    else:
        if card[2] not in chosen:
            chosen.add(card[2])
        elif card[3] not in chosen:
            chosen.add(card[3])

print(len(chosen))