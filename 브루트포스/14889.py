'''
문제
스타트와 링크
짝수 N명이 축구를 함.
N/2 명씩 팀을 이룸

번호를 1부터 N까지 배정
능력치 있음
Sij는 i와j가 같은 팀일때 팀에 더해지는 능력치 

Sij는 Sji와 다를 수도 있음
i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji


 능력치의 차이를 최소로

아이디어




'''
import sys 
from itertools import combinations

n = int(input())
scores = []
total = 0
min_diff = 1e10 
for i in range(n):
    line = list(map(int,sys.stdin.readline().split()))
    total+=sum(line)
    scores.append(line)

for team in combinations(range(n),n//2):
    result = 0
    for i,j in combinations(team,2):
        result += scores[i][j]+scores[j][i]
   
   
    team2 = list(range(n))
    for i in team:
        team2.remove(i)
    
    result2 = 0
    for i,j in combinations(team2,2):
        result2 += scores[i][j]+scores[j][i]

    min_diff = min(min_diff,abs(result2-result))

print(min_diff)