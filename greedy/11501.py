'''
문제
주식

매일 세가지 행동중 하나
1. 주식 하나 구매 
2. 원하는만큼 판매
3. 아무것도 안함

날 별로 주식의 가격을 알려주면 최적의 행동
'''
import sys
t = int(input())

for case in range(t):
    n = int(input())
    prices = list(map(int,input().split()))
    highest = 0
    result = 0
    for i in range(n-1,-1,-1):
        result += max(0,highest-prices[i])
        highest = max(highest,prices[i])
    print(result)




        

