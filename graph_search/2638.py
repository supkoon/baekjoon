from collections import deque
import sys

n,m = map(int,input().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dx = [-1,0,0,1]
dy = [0,1,-1,0]
cheezes=[]
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            cnt=0
            for d in range(4):
                i_new,j_new = i+dx[d],j+dy[d]
                if 0<=i_new<n and 0<=j_new<m and not graph[i_new][j_new]:
                    cnt+=1
                    if cnt==2:
                        cheezes.append([i,j])
                        break
def bfs():
    global visited,dx,dy,graph

    queue = deque()
    for i,j in cheezes:
        queue.append([i,j])
        visited[i][j]=1

    day=0
    while(queue):
        day+=1
        print(day,queue)
        length = len(queue)
        for i in range(length):
            x,y = queue.popleft()
            cnt=0
            for d in range(4):
                x_new,y_new = x+dx[d],y+dy[d]
                if 0 <= x_new < n and 0 <= y_new < m and not visited[x_new][y_new]:
                    if graph[x_new][y_new]==0:
                        cnt+=1
                        if cnt==2:
                            visited[x_new][y_new]=1
                            queue.append([x_new,y_new])
    return day

print(bfs())


