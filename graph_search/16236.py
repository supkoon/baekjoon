from collections import deque
n = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]
visited= [[0]*n for _ in range(n)]
size = 2
cnt=0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            start_x, start_y = i, j
        elif graph[i][j]:
             cnt+=1

#가장 가까운 물고기 --> bfs
#동률 << 상,좌 우선 bfs의 child를 sort? --> dx,dy 순서대로 하면 될듯. --> 01, -10, 0-1,10
#child의 조건 --> 자신의 크기 이하면 append,동시에 자기보다 작으면 visited

def bfs(start_x,start_y,graph):
    global visited
    global size
    global cnt
    cnt_eat=0
    cnt_moves=0
    queue= deque()
    queue.append([start_x,start_y])
    visited[start_x][start_y]=1
    if cnt ==0:
        return 0
    while(queue):
        print(1)
        x,y = queue.popleft()
        cnt_moves+=1
        for dx,dy in [(-1,0),(0,-1),(0,1),(1,0)]:
           x_new,y_new = x+dx,y+dy
           if 0<=x_new<n and 0<=y_new<n and not visited[x_new][y_new]:
               #길뚫기
               if graph[x_new][y_new]<=size:
                   queue.append([x_new,y_new])
                   #먹기
                   if graph[x_new][y_new]<size and graph[x_new][y_new]:
                       visited[x_new][y_new] = 1 #먹으면 다시 안가게
                       cnt_eat+=1 # 각 size별로 먹은 횟수 cnt
                       cnt-=1 # 남은 물고기 수 cnt
                       print(f"eat {x_new},{y_new}, size: {size}, cnt : {cnt_moves}")
                       if cnt ==0:
                           return cnt_moves
                       if cnt_eat==size:
                           size+=1 #size up
                           cnt_eat=0
    return cnt_moves

cnt_moves = bfs(start_x,start_y,graph)
print(cnt_moves)








