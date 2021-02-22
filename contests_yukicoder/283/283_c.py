import numpy as np
v, d = map(int, input().split())
e = np.array([list(map(int, list(input()))) for _ in range(v)], dtype=np.int64)
e_d = np.linalg.matrix_power(e, d)
print("Yes" if np.all(e_d != 0) else "No")