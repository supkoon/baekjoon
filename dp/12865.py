import sys
n,k = map(int,sys.stdin.readline().split())
nums= [[0,0]]
for i in range(n):
    nums.append(list(map(int,sys.stdin.readline().split())))

dp =[[0]*(k+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,k+1):
        w=nums[i][0]
        v=nums[i][1]
        if w>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(v+dp[i-1][j-w],dp[i-1][j])

print(dp[n][k])