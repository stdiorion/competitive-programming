w, h, x = map(int, input().split())
if x > 36:
    print(-1)

elif x == 0:
    for l in range(h):
        print("0" * w)

elif x <= 9:
    if w % 3 == 0:
        line1 = "0" + str(x) + "0"
    else:
        line1 = str(x) + "00"
    line1 *= w // 3 + 1
    line1 = line1[:w]
    lines = [line1, "0" * w, "0" * w]
    for l in range(h):
        print(lines[(l - int(h % 3 == 0)) % 3])

elif w > 1 and h > 1:
    if w % 3 == 2 and h % 3 == 2:
        line1 = str((x - 1) % 9 + 1) + str(int(x > 9) * 9) + "0"
        line1 *= w // 3 + 1
        line1 = line1[:w]
        line2 = str(int(x > 18) * 9) + str(int(x > 27) * 9) + "0"
        line2 *= w // 3 + 1
        line2 = line2[:w]
        line3 = "0" * w
        lines = [line1, line2, line3]
        for l in range(h):
            print(lines[l % 3])
    elif x <= 18:
        if w % 3 == 2:
            line1 = str((x - 1) % 9 + 1) + str(int(x > 9) * 9) + "0"
            line1 *= w // 3 + 1
            line1 = line1[:w]
            line2 = str(int(x > 18) * 9) + str(int(x > 27) * 9) + "0"
            line2 *= w // 3 + 1
            line2 = line2[:w]
            line3 = "0" * w
            lines = [line1, line2, line3]
            for l in range(h):
                print(lines[(l - int(h % 3 == 0)) % 3])
        elif h % 3 == 2:
            if w % 3:
                line1 = str((x - 1) % 9 + 1) + "00"
            else:
                line1 = "0" + str((x - 1) % 9 + 1) + "0"
            line1 *= w // 3 + 1
            line1 = line1[:w]
            if w % 3:
                line2 = str(int(x > 9) * 9) + "00"
            else:
                line2 = "0" + str(int(x > 9) * 9) + "0"
            line2 *= w // 3 + 1
            line2 = line2[:w]
            line3 = "0" * w
            lines = [line1, line2, line3]
            for l in range(h):
                print(lines[l % 3])
        else:
            print(-1)
    else:
        print(-1)

elif w == h == 1:
    if x > 9:
        print(-1)
    else:
        print(x)

elif w == 1:
    if x > 18:
        print(-1)
    elif x > 9:
        if h % 3 == 2:
            lines = [str((x - 1) % 9 + 1), str(int(x > 9) * 9), 0]
            for l in range(h):
                print(lines[l % 3])
        else:
            print(-1)
            
elif h == 1:
    if x > 18:
        print(-1)
    else:
        if w % 3 == 2:
            line1 = str((x - 1) % 9 + 1) + str(int(x > 9) * 9) + "0"
            line1 *= w // 3 + 1
            line1 = line1[:w]
            print(line1)
        else:
            print(-1)