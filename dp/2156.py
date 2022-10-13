import sys

n = int(sys.stdin.readline().rstrip())
nums =[]
for i in range(n):
    nums.append(int(sys.stdin.readline().rstrip()))

dp = [[0]*3 for _ in range(n)]
dp[0]=[nums[0],nums[0],0]
for i in range(1,n):
    for j in range(3):
        dp[i][0]=dp[i-1][2]+nums[i]
        dp[i][1]=dp[i-1][0]+nums[i]
        dp[i][2]=dp[i-1][1]
print(dp)
print(max(dp[n-1]))