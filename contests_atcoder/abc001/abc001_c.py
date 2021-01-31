from bisect import bisect_right
d, l = map(int, input().split())

w_list = [3, 16, 34, 55, 80, 108, 139, 172, 208, 245, 285, 327]
w_list = [(x * 10 - 5) * 6 // 10 for x in w_list]

w = bisect_right(w_list, l)

if w:
    dir = "N"
    if d < 113: dir = "N"
    elif d < 338: dir = "NNE"
    elif d < 563: dir = "NE"
    elif d < 788: dir = "ENE"
    elif d < 1013: dir = "E"
    elif d < 1238: dir = "ESE"
    elif d < 1463: dir = "SE"
    elif d < 1688: dir = "SSE"
    elif d < 1913: dir = "S"
    elif d < 2138: dir = "SSW"
    elif d < 2363: dir = "SW"
    elif d < 2588: dir = "WSW"
    elif d < 2813: dir = "W"
    elif d < 3038: dir = "WNW"
    elif d < 3263: dir = "NW"
    elif d < 3488: dir = "NNW"
    print(f"{dir} {w}")
else:
    print("C 0")