'''
문제
빙산
2차원 배열에 빙산
바다는 0 나머지 높이

빙산은 해마다 주변 바다의 수(동서남북) 만큼 줄어듬

한덩어리 빙산이 주어질때, 두 덩어리 이상으로 분리되는 최초의시간 구하기

아이디어
시뮬레이션 + bfs
매해 시뮬레이션을 진행함. 
--> 각 칸 주변에 몇개가 있는지.
--> graph를 카피해놓고 거기만 변형시키자. 


매 해 bfs 횟수를 cnt. 


복잡도
n3

'''
import sys
from collections import deque 
from copy import deepcopy
n, m = map(int, sys.stdin.readline().split())
graph = []

for i in range(n):
    line = list(map(int,sys.stdin.readline().split()))
    graph.append(line)

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(i,j):
    queue = deque()
    melting = deque()
    queue.append([i,j])
    visited[i][j] = 1 
   
    while(queue):
        x,y = queue.popleft()
        cnt= 0 
        for i in range(4):
            nx,ny = x+ dx[i],y+dy[i] 
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]:
                    if not visited[nx][ny]:
                        queue.append([nx,ny])
                        visited[nx][ny]=1
                else:
                    cnt +=1

        if cnt:
            melting.append([x,y,cnt])
    
    return melting


year =0 
while(True):
    visited = [[0]*(m) for _ in range(n)]
    cnt = 0 
    
    for i in range(n):
        for j in range(m):
            if graph[i][j]!=0 and not visited[i][j]:
                cnt+=1
                melted = bfs(i,j)
                for x,y,melt in melted:
                    graph[x][y] = max(graph[x][y]-melt,0)

    if cnt ==0:
        year = 0
        break
    if cnt >=2:
        break
    year+=1

print(year)
