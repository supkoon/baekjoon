'''
-아이디어
오름차순 정렬
cnt를 늘리면서 현재 공포도와 같으면 초기화

-복잡도 
O(n)


-변수
result : 길드 수
tgt : 현재 목표
cnt : 현재 수
'''

n = int(input())
people = list(map(int,input().split()))
people.sort()

result = 0
cnt = 0
for person in people:
    cnt+=1

    if person==cnt:
        result+=1
        cnt=0

print(result)

    


