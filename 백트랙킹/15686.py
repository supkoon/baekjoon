'''
문제
치킨배달
nxn 도시
빈칸, 치킨집, 집
치킨 거리 --> 집과 가장 가까운 치킨집사이의 거리 
가로 세로 거리 더하면됨.

도시의 치킨집 중 치킨 거리를 가장 작게 할 M개를 고름



아이디어
1.
완전탐색 + bfs?
완전탐색 : 치킨집 nCm 조합
백트래킹 : 치킨집 만날떄까지 bfs

permutation마다 map을 새로만들기. 
각 지점에서 시작해서 bfs를 통해 1을 만나는 순간 거리 return하기


2. 지점을 하나씩 더해감. 각 지점에서 집까지의 거리를 더해감. 만약 min보다 커지면 return + 가지치기
'''
import sys
from itertools import combinations
from collections import deque
import copy


def solution(n,m,chicken,houses):
    answer = 1e10
    for case in combinations(chicken,m):
        #m개만 선택
        result = 0 
        for k,l in houses: #집
            shortest = 1e10
            for i,j in case: #치킨집    
                distance = abs(i-k) + abs(j-l)
                shortest = min(distance,shortest)
            result += shortest
        answer = min(result,answer) 
    return answer

n,m = map(int,input().split())
graph = []
chicken = []
houses = []

for i in range(n):
        line = list(map(int,sys.stdin.readline().split()))
        for j in range(n):
            if line[j]==2:
                chicken.append([i,j])
                line[j]=0 #일부러 삭제함
            elif line[j]==1:
                houses.append([i,j])
        graph.append(line)

print(solution(n,m,chicken,houses))
