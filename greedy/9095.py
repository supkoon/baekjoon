'''
문제

n이 주어졌을 때 , 1,2,3의 합으로 나타내기 

#1,2,3의 합 

1 

2 
1 1  

3 
1 + 1 +1
1 + 2 
2 + 1 
2 + 2
'''


def solution(cases):
    n   = sorted(cases)[-1]
    dp = [0]*(n+1)
    dp[1] = 1 
    dp[2] = 2
    dp[3] = 4
    for i in range(4,n+1):
        dp[i] = dp[i-3] + dp[i-2] +dp[i-1]
    for i in cases:
        print(dp[i])
n = int(input())
cases = []
for i in range(n):
    cases.append(int(input()))
solution(cases)