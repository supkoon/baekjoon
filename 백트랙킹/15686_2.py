'''
문제
치킨거리 백트랙킹을 활용한 풀이

아이디어
한집씩 더해나감.

return 조건 1: 만약 현재 거리가 이전 최적보다 멀어지면 탐색안함 
return 조건 2: nCm m개 달성 시 탐색안함

'''

import sys 
answer = 1e10
def dfs(cur,chicken, houses,m,start): # cur:치킨좌표, houses: 집좌표, total_dist: 현재 거리 
    global answer
    #return 조건 
    if len(cur)==m:
        total_dist = 0
        for house_xy in houses:
            house_dist = 1e10 #각 집마다 최소거리 
            for chicken_xy in cur:
                house_dist = min(house_dist, abs(chicken_xy[0]-house_xy[0])+abs(chicken_xy[1]-house_xy[1]))
            total_dist+=house_dist
        answer = min(answer,total_dist)
        return 
    
    for child in range(start,len(chicken)):    
        cur.append(chicken[child])
        dfs(cur,chicken,houses,m,child+1)
        cur.pop()


def solution(n,m,graph):
    global answer 
    houses = []
    chicken = []
    for i in range(n):
        for j in range(n):
            if graph[i][j]==2:
                chicken.append([i,j])
            elif graph[i][j]==1:
                houses.append([i,j])
    dfs([],chicken,houses,m,0)
    return answer 
    
n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
print(solution(n,m,graph))


