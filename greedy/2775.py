'''
부녀회장 되려고 각 층 사람 모음
a층 b호에 살려면 아래층의 1호부터 b호까지 사람수만큼 데려와 살아야함

k층 n호?
'''



def solution(k,n):
    dp = [[0]*(n+1) for _ in range(k+1)]
    
    for i in range(k+1):
        for j in range(1,n+1):
            if i ==0: #0층은 j호에 j명
                dp[i][j]=j
            else: 
                dp[i][j] = sum(dp[i-1][:j+1])
    return dp[k][n]

t = int(input())
cases = [] 
for case in range(t):
    k = int(input())
    n = int(input())
    print(solution(k,n))

