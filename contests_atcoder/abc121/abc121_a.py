H, W = map(int, input().split())
h, w = map(int, input().split())
print(max(0, (H-h))*max(0,(W-w)))