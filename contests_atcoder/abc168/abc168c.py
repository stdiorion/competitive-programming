import math
A, B, H, M = map(int, input().split())

rotA = H / 12 + M / 720
rotB = M / 60
rad = abs(rotA - rotB) * 2 * math.pi

print((A * A + B * B - 2 * A * B * math.cos(rad)) ** 0.5)