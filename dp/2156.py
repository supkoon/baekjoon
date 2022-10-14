import sys

n = int(sys.stdin.readline())
nums =[]
for i in range(n):
    nums.append(int(sys.stdin.readline()))
dp = [[0]*3 for _ in range(n)]
dp[0]=[nums[0],nums[0],0]
for i in range(1,n):
    for j in range(3):
        dp[i][0]=dp[i-1][2]+nums[i]#이전꺼 안먹음
        dp[i][1]=dp[i-1][0]+nums[i]#이전꺼 먹음
        dp[i][2]=max(dp[i-1])#이번에 안먹어야함
print(max(dp[n-1]))