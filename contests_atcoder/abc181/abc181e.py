from bisect import bisect

n, m = map(int, input().split())

h = list(map(int, input().split()))
w = list(map(int, input().split()))

h.sort()
w.sort()

sumh_fw = [0]
sumh_bw = [0]

for i in range(0, len(h) - 1, 2):
    sumh_fw.append(h[i + 1] - h[i] + sumh_fw[-1])

for i in range(len(h) - 1, 0, -2):
    sumh_bw.append(h[i] - h[i - 1] + sumh_bw[-1])


ans = float("inf")

for teacher in w:
    t_pos = bisect(h, teacher)
    pair_t, t_is_taller = divmod(t_pos, 2)
    pair_t_diff = teacher - h[t_pos - 1] if t_is_taller else h[t_pos] - teacher
    ans = min(ans, sumh_fw[pair_t] + sumh_bw[-pair_t - 1] + pair_t_diff)

print(ans)