import sys
input = sys.stdin.readline

n, x = map(int, input().split())
subjects = [tuple(map(int, input().split())) for _ in range(n)]
