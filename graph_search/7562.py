import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
dx = [-1,-2,-2,-1,1,2,2,1]
dy = [-2,-1,1,2,-2,-1,1,2]

def bfs(start_x,start_y,end_x,end_y,m):
    queue=deque()
    visited = [[0]*m for _ in range(m)]
    queue.append([start_x,start_y])
    visited[start_x][start_y]=1
    while(queue):
        x,y = queue.popleft()
        for d in range(8):
            x_new,y_new =x+dx[d],y+dy[d]
            if 0<=x_new<m and 0<=y_new<m and not visited[x_new][y_new]:
                queue.append([x_new,y_new])
                visited[x_new][y_new]=visited[x][y]+1
    return visited[end_x][end_y]


for i in range(n):
    m = int(sys.stdin.readline().rstrip())
    s_x,s_y =  map(int,sys.stdin.readline().split())
    e_x,e_y = map(int,sys.stdin.readline().split())
    print(bfs(s_x,s_y,e_x,e_y,m)-1)


