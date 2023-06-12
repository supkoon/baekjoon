from collections import deque
def bfs(x,y):
    visited[x][y]=True
    queue = deque()
    queue.append([x,y])
    while(queue):
        x,y = queue.popleft()
        for dx,dy in [[-1,0],[1,0],[0,1],[0,-1]]:
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny]==0 and graph[nx][ny]:
                    visited[nx][ny] = visited[x][y]+1
                    queue.append([nx,ny])

n, m = map(int,input().split())

graph = []
for i in range(n):
    line = list(map(int,input()))
    graph.append(line)

visited = [[0] * m for _ in range(n)]

bfs(0,0)

print(visited[n-1][m-1])


