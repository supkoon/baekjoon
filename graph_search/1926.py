import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())

graph=[]
starts=[]
for i in range(n):
    line = list(map(int,sys.stdin.readline().split()))
    for j in range(m):
        if line[j]:
            starts.append([i,j])
    graph.append(line)

dx = [0,-1,1,0]
dy = [-1,0,0,1]
visited = [[0] * m for _ in range(n)]
def bfs(i,j):
    global graph,dx,dy,visited
    queue=deque()
    queue.append([i,j])
    visited[i][j]=1
    cnt=1
    while(queue):
        x,y=queue.popleft()
        for d in range(4):
            x_new,y_new=  x+dx[d],y+dy[d]
            if 0<=x_new<n and 0<=y_new<m and graph[x_new][y_new] and not visited[x_new][y_new]:

                queue.append([x_new,y_new])
                visited[x_new][y_new] = 1
                cnt+=1
    return cnt

cnt_drawing=0
cnt_max=0
for i,j in starts:
    if not visited[i][j]:
        cnt_drawing +=1
        cnt = bfs(i,j)
        cnt_max = max(cnt,cnt_max)
print(cnt_drawing)
print(cnt_max)


