dp = [0]*101

dp[1]=dp[2]=dp[3]=1
dp[4]=dp[5]=2

for case in range(int(input())):
    n = int(input())
    if dp[n]:
        print(dp[n])
    else:
        for i in range(6,n+1):
            if dp[i]:
                continue
            else:
                dp[i]= dp[i-1]+dp[i-5]
        print(dp[n])

