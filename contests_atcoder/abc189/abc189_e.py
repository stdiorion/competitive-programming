import numpy as np
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

points = []
addpoints = points.append

for _ in range(n):
    x, y = map(int, input().split())
    addpoints(np.array([x, y, 1], dtype = 'int64'))

m = int(input())

oper = [np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype = 'int64')]
addoper = oper.append
rotate1 = np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]], dtype = 'int64')
rotate2 = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]], dtype = 'int64')

for _ in range(m):
    op = input()
    tp = int(op[0])
    if tp == 1:
        addoper(np.dot(rotate1, oper[-1]))
    elif tp == 2:
        addoper(np.dot(rotate2, oper[-1]))
    elif tp == 3:
        p = int(op[2:])
        flip1 = np.array([[-1, 0, 2*p], [0, 1, 0], [0, 0, 1]], dtype = 'int64')
        addoper(np.dot(flip1, oper[-1]))
    elif tp == 4:
        p = int(op[2:])
        flip2 = np.array([[1, 0, 0], [0, -1, 2*p], [0, 0, 1]], dtype = 'int64')
        addoper(np.dot(flip2, oper[-1]))

Q = int(input())

for _ in range(Q):
    i, point = map(int, input().split())
    res = np.dot(oper[i], points[point-1])[:2]
    print(*res)