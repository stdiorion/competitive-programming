""" 
多分dpだと想います。

埋める配列
dp[i] = i文字目までを埋める組み合わせの総数

漸化式
dp[0] = 1
dp[i] = dp[i] + dp[i - len(phrase)] + 1 if spell[i - len(phrase) : i] == phrase

埋める順番
iを1から
 """

MOD = 1000000007

n = int(input())
spell = input().rstrip()
phrase = [input().rstrip() for _ in range(n)]

dp = [1] + [0] * len(spell)

for i in range(1, 1 + len(spell)):
    for p in phrase:
        if len(p) <= i and spell[i - len(p) : i] == p:
            dp[i] += dp[i - len(p)]
            dp[i] %= MOD

print(dp[-1])