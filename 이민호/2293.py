n, k = map(int, input().split())
stack = []
dp = [0] * 10001
for _ in range(n):
    tmp = int(input())
    stack.append(tmp)
dp[0] = 1
stack.sort()
for s in stack:
    for i in range(s, k + 1):
        if i - s >= 0:
            dp[i] += dp[i - s]
print(dp[k])