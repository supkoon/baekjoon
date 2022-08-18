from collections import deque
n = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]
size = 2
cnt_food=0
cnt_eat = 0
cnt_moves=0
flag=False
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            start_x, start_y = i, j
            graph[i][j]=0
        elif graph[i][j]:
             cnt_food+=1

def bfs(graph):
    global size
    global cnt_food
    global cnt_eat
    global cnt_moves
    global start_x,start_y
    global flag
    visited = [[0] * n for _ in range(n)]
    queue= deque()
    queue.append([start_x,start_y])
    visited[start_x][start_y]=1
    candidates=[]
    while(queue):
        x,y = queue.popleft()
        for dx,dy in [(-1,0),(0,-1),(0,1),(1,0)]:
           x_new,y_new = x+dx,y+dy
           if 0<=x_new<n and 0<=y_new<n and not visited[x_new][y_new]:
               if graph[x_new][y_new]<=size:
                   visited[x_new][y_new] = visited[x][y] + 1
                   queue.append([x_new,y_new])
                   if 1<=graph[x_new][y_new]<size:
                       candidates.append([x_new,y_new])
    if candidates:
        candidates.sort(key=lambda x: [visited[x[0]][x[1]], x[0], x[1]])
        x_new,y_new = candidates[0]
        graph[x_new][y_new] = 0
        start_x, start_y = x_new, y_new
        cnt_moves += visited[x_new][y_new] - 1
        cnt_eat += 1
        cnt_food -= 1
        if cnt_eat == size:
            size += 1
            cnt_eat = 0
    else:
        if cnt_moves:
            print(cnt_moves)
            flag=True
        else:
            print(0)
            flag=True

while(True):
         bfs(graph)
         if flag:
             break











