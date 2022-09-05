from collections import deque
n = int(input())
graph = [list(map(int,list(input()))) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
dx = [0,-1,1,0]
dy = [-1,0,0,1]


cnt_group=0
cnt_each=[]
def bfs(i,j,graph):
    global visited,dx,dy,cnt_group,cnt_each
    queue=deque()
    queue.append([i,j])
    visited[i][j]=1
    cnt=1
    while(queue):
        x,y = queue.popleft()
        for d in range(4):
            x_new,y_new = x+dx[d],y+dy[d]
            if 0<=x_new<n and 0<=y_new<n and not visited[x_new][y_new]:
                if graph[x_new][y_new]:
                    queue.append([x_new,y_new])
                    visited[x_new][y_new]=visited[x][y]+1
                    cnt+=1
    cnt_group+=1
    cnt_each.append(cnt)

for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j]:
            bfs(i,j,graph)

print(cnt_group)
for i in sorted(cnt_each):
    print(i)