""" 
多分dpだと想います。


埋める配列
dp[i][j] = 水が100ig、砂糖がjgという入れ方が可能なら1不可能なら0

漸化式
dp[0][0] = True
dp[i][j] = dp[i-a][j] or dp[i-b][j] or dp[i][j-c] or dp[i][j-d]
            and 100i + j <= f

if 100 * i * e >= j: j/(i+j)の最大値更新 i,jも記録

埋める順番
iを1から
 jを1から
 """


a, b, c, d, e, f = map(int, input().split())

water_max = f // 100
sugar_max = water_max * e

# dp[i][j] = 水100ig、砂糖jgという入れ方が可能かどうか
dp = [[False] * (sugar_max + 1) for _ in range(water_max + 1)]
dp[0][0] = True

maxdensity = -1
ans = "0 0"

for i in range(water_max + 1):
    for j in range(sugar_max + 1):
        if i == j == 0:
            continue
        # ビーカー容量内
        if 100 * i + j <= f:
            dp[i][j] = (i-a >= 0 and dp[i-a][j]) or (i-b >= 0 and dp[i-b][j]) or\
                       (j-c >= 0 and dp[i][j-c]) or (j-d >= 0 and dp[i][j-d])
        
        # 溶け残りがない かつ 砂糖だけじゃない
        if dp[i][j] and i * e >= j and i != 0:
            density = j / (i + j)
            if density > maxdensity:
                maxdensity = density
                ans = str(100 * i + j) + " " + str(j)

print(ans)