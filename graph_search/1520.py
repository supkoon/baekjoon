'''
문제
지도가 있음.
각 지점의 높이를 나타냄.
상하좌우로 이동가능.
0,0에서 n-1xn-1로 가려고함.

항상 높이가 더 낮은 지점으로만 이동
--> 경우의 수가 다양.

아이디어
bfs  + 우선순위큐(heapq) +  dp 

복잡도
'''
import sys
from collections import deque
import heapq 
graph = [] 
n,m = map(int, sys.stdin.readline().split())
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

visited = [[0]*m for _ in range(n)]

def bfs(i,j):
    queue = list()

    visited[i][j]=1
    heapq.heappush(queue,[-graph[i][j],i,j])

    while(queue):
        cnt,x,y = heapq.heappop(queue)
        
        for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
            nx,ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<m:
                if graph[x][y] > graph[nx][ny]:
                    #방문을 안했으면 탐색할 큐(경로)에 추가하면서 횟수 더하기
                    if not visited[nx][ny]:
                        heapq.heappush(queue,[-graph[nx][ny],nx,ny])
                    #이미 방문 했으면 횟수만 더해주기. 
                    visited[nx][ny] +=visited[x][y]     
                    
bfs(0,0)
print(visited[n-1][m-1])