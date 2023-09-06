'''
문제
0으로 시작하지 않는 이진수
1이 두번연속 안나타나는 이진수  (11없음)

N자리 이친수의 수 

이어만드는거는 거의 dp같음. 


'''

def solution(n):

    dp = [0]*(91)
    dp[1]=1
    dp[2]=1
    dp[3]=2

    for i in range(4,n+1):
        dp[i] = dp[i-1]+dp[i-2]
    
    return dp[n]

n = int(input())
print(solution(n))