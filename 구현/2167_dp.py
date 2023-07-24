import sys
n,m = map(int,sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

k = int(input())
dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = arr[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]
#위의 누적합 + 아래의 누적합 - 겹치는부분 + 현재부분 


for i in range(k):
    i,j,x,y = map(int,sys.stdin.readline().split())
    result = dp[x][y]-dp[x][j-1]-dp[i-1][y]+dp[i-1][j-1]
    print(result)