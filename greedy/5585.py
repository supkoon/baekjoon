'''
문제
거스름돈.
가장 동전수 적게.


아이디어
그리디
당연히 가장 큰 돈부터 몫,나머지

복잡도
O(상수)

'''

n = 1000-int(input())

result = 0
coins = [500,100,50,10,5,1]

for coin in coins:
    if n//coin:
        result+= n//coin
        n = n %coin
print(result)

