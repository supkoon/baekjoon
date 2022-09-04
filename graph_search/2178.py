from collections import deque
n,m = map(int,input().split())

graph = [list(map(int,list(input()))) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
visited[0][0]=1
dx = [0,-1,1,0]
dy = [-1,0,0,1]

def bfs(graph):
    global dx,dy,visited
    queue=deque()
    queue.append([0,0])
    while(queue):
        x,y = queue.popleft()
        for d in range(4):
            x_new,y_new = x+dx[d],y+dy[d]
            if 0<=x_new<n and 0<=y_new<m and not visited[x_new][y_new]:
                if graph[x_new][y_new]:
                    queue.append([x_new,y_new])
                    visited[x_new][y_new]=visited[x][y]+1

bfs(graph)
print(visited[n-1][m-1])