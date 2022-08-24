from collections import deque
m,n = map(int,input().split())

graph = []
tomatos=[]
left=0
visited = [[0]*m for _ in range(n)]
for i in range(n):
    line = list(map(int,input().split()))
    graph.append(line)
    for j in range(m):
        if line[j]==1:
          tomatos.append([i,j])
          visited[i][j]=1
        elif line[j]==0:
            left+=1


day = 0
dx = [-1,0,0,1]
dy = [0,1,-1,0]


def bfs():
    global graph,tomatos,visited,left,day,dx,dy
    queue= deque()
    for tomato in tomatos:
        queue.append(tomato)
    flag=0
    while(queue):
        if left==0:
            break
        day_length = len(queue)
        moves_day=[]
        day+=1
        for i in range(day_length):
            x,y = queue.popleft()
            for move in range(4):
                x_new,y_new = x+dx[move],y+dy[move]
                if 0<=x_new<n and 0<=y_new<m and not visited[x_new][y_new]:
                    #0이상이면 이동
                    visited[x_new][y_new] = 1
                    if graph[x_new][y_new]>=0:
                        queue.append([x_new,y_new])
                        #그 중 안익은 토마토라면
                        if graph[x_new][y_new]==0:
                            left-=1
                            graph[x_new][y_new]=1
                            if left==0:
                                flag=1
                                break
        if flag:break

bfs()
if left:
    print(-1)
else: print(day)