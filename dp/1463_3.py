'''
문제
X가 3으로 나눠 떨어지면 3으로 나눔
X가 2로 나누어 떨어지면 2로 나눔
1을 뻄

1을 만드는 최소 횟수

아이디어
자식이 셋인데 N이 ㅈㄴ 크고 시간제한은 0.15-> 이거탐색은 아님 
'''

def solution(n):
    dp = [0] * (n+1)    
    #1부터 만들어가자 
    for i in range(2,n+1):
        if i%3==0 and i%2==0:
            dp[i] = min(dp[i//3],dp[i//2],dp[i-1])+1
        elif i%3==0:
            dp[i] = min(dp[i//3],dp[i-1])+1
        elif i%2==0: 
            dp[i] = min(dp[i//2],dp[i-1])+1
        else:
            dp[i] = dp[i-1]+1

    return dp[n]
n = int(input())
print(solution(n))

#1 3 9 10 


