'''
문제
2xn 직사각형을 1x2, 2x1, 2x2로 채우는 방법의 수를 계산 


아이디어
DP..
앞에서부터 규칙 찾자..



복잡도

'''

n = int(input())

dp = [0]*(n+1)

dp[1] = 1
dp[2] = 3

for i in range(3,n+1):
    dp[i] = 2*dp[i-2]+dp[i-1]

print(dp[n]%10007)