import sys
from collections import deque
m , n = map(int,sys.stdin.readline().split())
graph = [list(input()) for line in range(m)]
visited = [[False] * n for _ in range(m)]
dx = [-1,0,0,1]
dy = [0,1,-1,0]

def bfs(x,y,graph):
    global visited
    queue = deque()
    queue.append([x,y])
    visited[x][y]=True
    while(queue):
        x,y = queue.popleft()
        for i in range(4):
            x_= x+dx[i]
            y_= y+dy[i]
            if 0<=x_<m and 0<=y_<n:
                if graph[x_][y_]=='0' and not visited[x_][y_] :
                    queue.append([x_,y_])
                    visited[x_][y_]=True

result = False
for col in range(n):
    if graph[0][col]=='0':
        bfs(0,col,graph)
    if sum(visited[-1])>0:
        print('YES')
        exit()
print('NO')

#visited를 안쓰고 graph[x][y] 를 2로 바꾸면 메모리 아낄듯.

