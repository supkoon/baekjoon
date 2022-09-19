from collections import deque
import sys

n,m = map(int,input().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dx = [-1,0,0,1]
dy = [0,1,-1,0]
day=0

def bfs():
    global dx,dy,graph,day
    queue = deque()
    queue.append([0,0])
    visited[0][0]=1
    while queue:
        x,y = queue.popleft()
        for d in range(4):
            x_new,y_new = x+dx[d],y+dy[d]
            if  0 <= x_new < n and 0 <= y_new < m and not visited[x_new][y_new]:
                if graph[x_new][y_new]:
                    graph[x_new][y_new]+=1
                else :
                    #0일때
                    visited[x_new][y_new]=1
                    queue.append([x_new,y_new])
time=0
while True:
    visited = [[0] * m for _ in range(n)]
    bfs()
    flag=0
    for i in range(n):
        for j in range(m):
            if graph[i][j]>=3:
                graph[i][j]=0
                flag=1
            elif graph[i][j]==2:
                graph[i][j]=1
    if flag:
        time+=1
    else:
        break
print(time)

