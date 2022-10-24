import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())
graph = []
for i in range(n):
    line= list(map(int,list(sys.stdin.readline().rstrip())))
    graph.append(line)

dx =[0,-1,1,0]
dy =[-1,0,0,1]

visited = [[[0]*2  for i in range(m)] for _ in range(n)]
#통과하면 칸수, 못통과하면 -1
def bfs():
    global graph,dx,dy,visited
    queue=deque()
    queue.append([0,0,0])
    visited[0][0][0]=1
    while(queue):
        x,y,cnt=queue.popleft()
        if x ==n-1 and y ==m-1:
                return visited[x][y][cnt]
        for d in range(4):
            x_new,y_new = x+dx[d],y+dy[d]
            if 0<=x_new<n and 0<=y_new<m :
                if cnt == 0 and graph[x_new][y_new]:
                    visited[x_new][y_new][1] = visited[x][y][0] + 1
                    queue.append([x_new, y_new, 1])
                elif visited[x_new][y_new][cnt]==0 and  graph[x_new][y_new]==0:
                        queue.append([x_new,y_new,cnt])
                        visited[x_new][y_new][cnt] = visited[x][y][cnt] + 1

    return -1
print(bfs())