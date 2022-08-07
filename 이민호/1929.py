import sys
m, n = map(int, sys.stdin.readline().split())
dp = [0]*1000001
for i in range(m, n+1):
    dp[i] = i

for i in range(2, n+1):
    if dp[i] == -1:
        continue
    for j in range(2 * i, n + 1, i):
        dp[j] = -1
for i in range(m, n+1):
    if i == 1:
        continue
    if dp[i] != -1:
        print(dp[i])
