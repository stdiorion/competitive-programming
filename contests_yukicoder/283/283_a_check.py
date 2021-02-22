from random import randint

def solve(h, w, x):
    if x > 36:
        return (-1)

    elif x <= 9:
        if w % 3 == 0:
            line1 = "0" + str(x) + "0"
        else:
            line1 = str(x) + "00"
        line1 *= w // 3 + 1
        line1 = line1[:w]
        lines = [line1, "0" * w, "0" * w]
        return [lines[(l - int(h % 3 == 0)) % 3] for l in range(h)]

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
            return [lines[l % 3] for l in range(h)]
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
                return [lines[(l - int(h % 3 == 0)) % 3] for l in range(h)]
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
                
                return [lines[l % 3] for l in range(h)]
            else:
                return (-1)
        else:
            return (-1)

    elif w == h == 1:
        if x > 9:
            return (-1)
        else:
            return [x]

    elif w == 1:
        if x > 18:
            return (-1)
        elif x > 9:
            if h % 3 == 2:
                lines = [str((x - 1) % 9 + 1), str(int(x > 9) * 9), "0"]
                return [lines[l % 3] for l in range(h)]
            else:
                return (-1)
                
    elif h == 1:
        if x > 18:
            return (-1)
        else:
            if w % 3 == 2:
                line1 = str((x - 1) % 9 + 1) + str(int(x > 9) * 9) + "0"
                line1 *= w // 3 + 1
                line1 = line1[:w]
                return [line1]
            else:
                return (-1)

def check(h, w, x, ans):
    if ans == -1:
        return True
    for i in range(h):
        for j in range(w):
            power = int(ans[i][j])
            if i - 1 >= 0: power += int(ans[i - 1][j])
            if i + 1 < h: power += int(ans[i + 1][j])
            if j - 1 >= 0: power += int(ans[i][j - 1])
            if j + 1 < w: power += int(ans[i][j + 1])
            if i - 1 >= 0 and j - 1 >= 0: power += int(ans[i - 1][j - 1])
            if i - 1 >= 0 and j + 1 < w: power += int(ans[i - 1][j + 1])
            if i + 1 < h and j - 1 >= 0: power += int(ans[i + 1][j - 1])
            if i + 1 < h and j + 1 < w: power += int(ans[i + 1][j + 1])
            if power != x:
                return False
    return True

for _ in range(1000):
    h = randint(1, 10)
    w = randint(1, 10)
    x = randint(1, 40)
    if not check(h, w, x, solve(h, w, x)):
        print(h, w, x)