import sys
n,m = map(int,input().split())
prices = []
max_prices=-1
for i in range(m):
    price = int(sys.stdin.readline().rstrip())
    prices.append(price)
    if price>max_prices:
        max_prices=price
prices.sort(reverse=True)
#비싼가격일수록 조금팔수있음 --> 가격은 reverse로 down, 갯수는 up
max_result =0
max_price=0
for i in range(m):
  if i+1 > n:
      break
  each_result = prices[i]*(i+1)
  if each_result > max_result:
            max_result = each_result
            max_price = prices[i]
print(max_price,max_result)
