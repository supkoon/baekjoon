'''
문제
지도가 있음.
각 지점의 높이를 나타냄.
상하좌우로 이동가능.
0,0에서 n-1xn-1로 가려고함.

항상 높이가 더 낮은 지점으로만 이동
--> 경우의 수가 다양.

아이디어
bfs?  



복잡도


'''
import sys
from collections import deque
graph = [] 
n,m = map(int, sys.stdin.readline().split())
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

visited = [[0]*m for _ in range(n)]

def bfs(i,j):
    queue = deque()
    visited[i][j]=1
    queue.append([i,j])
    while(queue):
        x,y = queue.popleft()
        for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
            nx,ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<m:
                if graph[x][y] > graph[nx][ny]:
                    if not visited[nx][ny]:
                        queue.append([nx,ny])
                        visited[nx][ny] = 1     

bfs(0,0)
for x in range(n):
    for y in range(m):
        if visited[x][y]:
            cnt= 0 
            for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                nx,ny = x+dx,y+dy
                if 0<=nx<n and 0<=ny<m and visited[nx][ny]:
                    if graph[nx][ny] > graph[x][y]:
                        cnt += visited[nx][ny]
            visited[x][y] = max(1,cnt) 

print(visited[n-1][m-1])
