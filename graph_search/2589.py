# 보물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다.
# 보물 위치 사이의 최단거리?

import sys
from collections import deque
n, m = map(int,sys.stdin.readline().split())
t = []
graph = []
starts=[]
for i in range(n):
    line = list(sys.stdin.readline().rstrip())
    for j in range(m):
        if line[j]=='L':
            starts.append([i,j])
    graph.append(line)
dx = [-1,0,0,1]
dy = [0,-1,1,0]

def bfs(start_i,start_j):
    global dx,dy,graph
    visited = [[0]*m for _ in range(n)]
    visited[start_i][start_j]=1
    queue = deque()
    queue.append([start_i,start_j])
    max_cnt=1
    while(queue):
        x,y = queue.popleft()
        for d in range(4):
            x_new,y_new = x+dx[d],y+dy[d]
            if 0<=x_new<n and 0<=y_new<m and graph[x_new][y_new]=='L' and not visited[x_new][y_new]:
                queue.append([x_new,y_new])
                visited[x_new][y_new]=visited[x][y]+1
                if visited[x_new][y_new] > max_cnt:
                    max_cnt = visited[x_new][y_new]
    return max_cnt
max_cnt = 1
for i,j in starts:
    cnt = bfs(i,j)
    if max_cnt<cnt:
        max_cnt=cnt

print(max_cnt-1)

