n,m = map(int,input().split())
nums = [0]+list(map(int,input().split()))
cases=[]
for case in range(m):
    i,j = map(int,input().split())
    cases.append([i,j])
dp = [0]*(n+1)
for i in range(1,n+1):
    dp[i]=dp[i-1]+nums[i]
for i,j in cases:
    print(dp[j]-dp[i-1])
