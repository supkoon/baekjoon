n = int(input())
dp = [0]*(10**6)

1#1
2#11,2
3#111 ,12,21, 3
4#1111 112 121 211 22 13 31
5#11111 1112 1121 1211 2111 122 221 212 131 113 311 32 23
# 1 2 4 7 13
dp[1]=1
dp[2]=2
dp[3]=4
for case in range(n):
    num = int(input())
    if dp[num]:
        print(dp[num])
    else:
        for i in range(4,num+1):
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
        print(dp[num])

