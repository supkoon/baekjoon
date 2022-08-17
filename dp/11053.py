n = int(input())
arr = list(map(int,input().split()))
dp = [1 for _ in range(n)]

result=1
for i in range(n):
    for j in range(i,n):
        if arr[i]<arr[j]:
            dp[j]=max(dp[i]+1,dp[j])
            if dp[j]>result:
                result = dp[j]
print(result)

