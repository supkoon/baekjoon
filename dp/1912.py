n = int(input())
arr = list(map(int, input().split()))
dp = [0] * ((10 ** 5) + 1)
dp[0] = arr[0]
max = arr[0]
for i in range(1, n):
    if dp[i - 1] > 0:
        dp[i] = dp[i - 1] + arr[i]
    else:
        dp[i] = arr[i]
    if dp[i] > max:
        max = dp[i]
print(max)
