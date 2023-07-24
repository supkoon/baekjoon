'''
문제
등수 구하기
노래마다 랭킹이 내림차순임.
같은 점수가 이미 있으면 그 점수의 등수 중에서 가장 아래 점수로 따짐. 

이미 랭킹리스트가 있을 때,
태수의 등수는 ? 
P보다 밖이면 -1


아이디어
사전에 길이가 꽉 찼으면서, 마지막거보다 작거나 같으면 -1 출력하고

아닌경우, for문으로 지나면서 점수랑 비교.

복잡도
O(n)

변수
p 점수의 수
N 리스트에 이미 있는 점수 수 

'''

n, new_score, p = map(int,input().split())
if n == 0:
    print(1)

else:
    scores = list(map(int,input().split()))
    
    if n == p and scores[-1] >= new_score :
        print(-1)
    
    else:
        rank = n+1
        for i in range(n):
            if scores[i] <= new_score:
                rank = i + 1
                break
        print(rank)
