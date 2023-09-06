'''
문제
오름차순을 이루는 수 (이상)
수의 길이 N개가 있을떄, 오르막의 수 


아이디어
완전탐색은 어려워보임 
(55-i)?         

'''

def solution(n):
    dp = [[0]*10 for _ in range(1001)]
    for i in range(1,n+1):
        for j in range(10):
            if i ==1:
                dp[i][j] = 1
            else:
                if j==0:
                    dp[i][j]=sum(dp[i-1])
                else:
                    dp[i][j]=dp[i][j-1] - dp[i-1][j-1] 


    return sum(dp[n])%10007
#10007로 나눈 나머지 
n = int(input())
print(solution(n))
