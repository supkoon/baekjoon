'''
문제
카드구매하기
ps카드 모으기
색칠되어있음

1~n개가 들어있는 카드팩 n가지 있음

개수가 적어도 비싸면 좋을것같아서 n개 구매하려함.

돈을 최대한 많이 지불
카드가 i개 포함된 카드팩의 가격은 Pi원이다.

i개 들어있는 카드팩과 가격 있을때, 최대소비
딱맞춰야함 

아이디어

1초 N~1000
dp 행렬의 idx : 개수
dp 행렬의 값 : 가격, 최대니깐 max 들어갈듯 
'''

def solution(n,cards):
    dp = [0]*(n+1)
    for i in range(len(cards)):
        dp[i+1] = cards[i]
    
    for i in range(2,n+1): #n장까지 소모 
        for j in range(1,i): #카드 소모 수 
            #이미 i장 샀음. n-i장까지 가능 
            dp[i] = max(dp[i], dp[i-j]+dp[j])
        
    return(dp[n])

n = int(input())
cards = list(map(int,input().split()))
print(solution(n,cards))