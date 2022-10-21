from collections import deque
import sys
n = int(sys.stdin.readline())
graph = []
max_depth = 0
dx = [0,-1,1,0]
dy = [-1,0,0,1]
for i in range(n):
    line = list(map(int,sys.stdin.readline().split()))
    a= max(line)
    if max_depth<a:
        max_depth=a
    graph.append(line)

def bfs(i,j,max_depth):
    global graph,dx,dy,visited,cnt
    queue=deque()
    queue.append([i,j])
    visited[i][j]=1
    while(queue):
        x,y = queue.popleft()
        for d in range(4):
            x_new,y_new = x+dx[d],y+dy[d]
            if 0<=x_new<n and 0<=y_new<n and not visited[x_new][y_new]:
                if graph[x_new][y_new]>max_depth:
                    queue.append([x_new,y_new])
                    visited[x_new][y_new]=1
    cnt+=1

cnt_max=1
for depth in range(1,max_depth):
    cnt=0
    visited = [[0] * n for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if not visited[j][k] and graph[j][k]>depth:
                bfs(j,k,depth)
    if cnt>cnt_max:
        cnt_max=cnt
print(cnt_max)

