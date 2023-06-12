from collections import deque
import time
t1 = time.time()
n,m = map(int,input().split())
graph = [[] for _ in range(n)]
visited = [[0] * m for _ in range(n)]

cnt = 0 
for i in range(n):
    line = list(map(int,input()))
    graph[i] = line

def bfs(i,j):
    global graph,visited,cnt,m,n
    visited[i][j]=1
    queue = deque()
    queue.append([i,j])
    while(queue):
        x,y = queue.popleft()
        for dx,dy in [[-1,0],[1,0],[0,1],[0,-1]]:
            nx = x+dx
            ny = y+dy
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny] == 0 and graph[nx][ny]==0:
         
                    queue.append([nx,ny])
                    visited[nx][ny]=1
    cnt+=1

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0  and graph[i][j]==0:
            bfs(i,j)
t2 = time.time()
print(t2-t1)
print(cnt)

