from collections import deque
n = int(input())

graph = []
for i in range(n):
    line = list(input())
    graph.append(line)
visited = [[0]*n for _ in range(n)]
visited2 = [[0]*n for _ in range(n)]
dx = [-1,0,0,1]
dy = [0,-1,1,0]
cnt=0
cnt2=0
def bfs(i,j,eyeproblem=False):
    global visited,graph,dx,dy,cnt,cnt2
    queue=deque()
    queue.append([i,j])
    if eyeproblem:
        visited2[i][j] =1
        cnt2+=1
    else:
        visited[i][j]=1
        cnt+=1

    color = graph[i][j]

    if eyeproblem==False:
        while(queue):
            x,y = queue.popleft()
            for d in range(4):
                new_x,new_y= x+dx[d],y+dy[d]
                if 0<=new_x<n and 0<=new_y<n and graph[new_x][new_y]==color and not visited[new_x][new_y]:
                    queue.append([new_x,new_y])
                    visited[new_x][new_y]=1
    else:
        while(queue):
            x,y = queue.popleft()
            for d in range(4):
                new_x, new_y = x + dx[d], y + dy[d]
                if 0 <= new_x < n and 0 <= new_y < n and not visited2[new_x][new_y]:
                    if graph[x][y]=='R' or graph[x][y]=='G':
                        if graph[new_x][new_y] != 'B':
                            queue.append([new_x, new_y])
                            visited2[new_x][new_y] = 1
                    else:
                        if graph[new_x][new_y] == color:
                            queue.append([new_x, new_y])
                            visited2[new_x][new_y] = 1


for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
        if not visited2[i][j]:
            bfs(i,j,eyeproblem=True)
print(cnt,cnt2)
