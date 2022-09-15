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
    day=0
    while(queue):
        result = 0
        for i in graph:
            result += sum(i)
        if not result:
            return day
        day+=1
        length = len(queue)
        change_list = []
        for i in range(length):
            x,y = queue.popleft()
            cnt=0
            add_list = []
            for d in range(4):
                x_new,y_new = x+dx[d],y+dy[d]
                if  0 <= x_new < n and 0 <= y_new < m :
                    if not graph[x_new][y_new]:
                        cnt+=1
                    else:
                        add_list.append([x_new,y_new])
            if cnt>=2:
                visited[x][y]=1
                change_list.append([x,y])
                for i in add_list:
                    queue.append(i)
        for i,j in change_list:
            graph[i][j]=0
print(bfs())


