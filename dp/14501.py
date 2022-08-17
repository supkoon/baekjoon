n = int(input())
arr = []
dp = [0 for _ in range(n+1)]
for i in range(n):
    day,pay = map(int,input().split())
    arr.append([day,pay])

for i in range(n-1,-1,-1):
    if i+arr[i][0]>n:
        dp[i]=dp[i+1]
    else:
        dp[i] = max(dp[i+1],arr[i][1]+dp[i+arr[i][0]])

print(dp[0])
