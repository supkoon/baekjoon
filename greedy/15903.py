'''
문제
카드합체놀이
n장
x,y번 카드 골라서 더함
x+y를 각각에 덮어씀
m번반복
만들수 있는 가장 작은 점수


아이디어
그리디


'''


n,m = map(int,input().split())
cards = list(map(int,input().split()))

for i in range(m):
    cards.sort()
    cards[0], cards[1] = cards[0]+cards[1],cards[0]+cards[1]
    
print(sum(cards))
