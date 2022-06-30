import sys
from collections import deque
n, m  = map(int,sys.stdin.readline().split())
war_map = [list(sys.stdin.readline().rstrip()) for _ in range(m)]

dx=[-1,0,0,1]
dy=[0,1,-1,0]
visited = [[0 for col in range(n)] for _ in range(m)]
total_W = 0
total_B = 0
def bfs(i,j,graph):
    mark = graph[i][j]
    cnt=0
    queue = deque()
    queue.append([i,j])
    visited[i][j]=1
    while(queue):
        x,y = queue.popleft()
        for child in range(4):
            new_x = x + dx[child]
            new_y = y + dy[child]
            if 0<=new_x<m and 0<=new_y<n:
                if graph[new_x][new_y]==mark and not visited[new_x][new_y]:
                    queue.append([new_x,new_y])
                    visited[new_x][new_y]=1
                    cnt+=1
    return (cnt+1)**2

for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            if war_map[i][j]=='W':
                total_W += bfs(i,j,war_map)
            else:
                total_B += bfs(i,j,war_map)
print(total_W,total_B)



