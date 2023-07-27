'''
문제
N개 도시가 일직선
기름을 넣고 왼쪽에서 출발
기름통 제한 x
1km당 1리터
도시에는 하나의 주유소
도시마다 기름가격 다름




아이디어
매번 최소 가격을 기억하면서 갱신.
부족한만큼 최소가격을 불러와서 채움. 


복잡도
o(n)


'''
n = int(input())
loads = list(map(int,input().split()))
prices = list(map(int,input().split()))

total_price = 0 
min_price = 1e10
for idx in range(len(loads)):
    need = loads[idx]
    min_price = min(min_price, prices[idx])
    total_price += min_price * need
print(total_price)