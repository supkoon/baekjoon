from collections import deque
n,m = map(int, input().split())


graph = [list(map(int,list(input()))) for _ in range(n)]
n_house = 0
house = []
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            house.append([i,j])
            n_house+=1
dx = [-1,0,0,1]
dy = [0,1,-1,0]

def bfs(i,j,k,l,graph):
    queue = deque()
    queue.append([i,j])
    queue.append([k,l])
    visited = [[0]*m for _ in range(n)]
    visited[i][j]=1
    visited[k][l]=1
    while(queue):
        x,y = queue.popleft()
        for index in range(4):
            new_x = x+dx[index]
            new_y = y+dy[index]
            if 0<=new_x<n and 0<=new_y<m:
                if not visited[new_x][new_y]:
                    queue.append([new_x,new_y])
                    visited[new_x][new_y]=visited[x][y]+1
    return visited
min_global = 1000
for i in range(n):
    for j in range(m):
        if not graph[i][j]:
            for k in range(i,n):
                for l in range(j,m):
                    if not graph[k][l]:
                        if i==k and j==l:continue
                        else:
                            visited=bfs(i,j,k,l,graph)
                            # print(i,j,k,l,visited)
                            max_each = 0
                            for house_x,house_y in house:
                                if max_each < visited[house_x][house_y]:
                                    max_each = visited[house_x][house_y]
                            if min_global > max_each:
                                min_global = max_each
print(min_global-1)








