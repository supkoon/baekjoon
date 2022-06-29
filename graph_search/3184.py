import sys
from collections import deque
r,c = map(int,sys.stdin.readline().split())
farm_map =[list(sys.stdin.readline().rstrip()) for line in range(r)]
graph = [[[] for col in range(c)] for row in range(r)]
dx = [-1,0,0,1]
dy = [0,1,-1,0]

for i in range(r):
    for j in range(c):
        if farm_map[i][j]!='#':
            for direction in range(4):
                i_new = i+dx[direction]
                j_new = j+dy[direction]
                if 0<=i_new<r and 0<=j_new<c and farm_map[i_new][j_new]!='#':
                    graph[i][j].append([i_new,j_new])
visited = [[False for col in range(c)] for row in range(r)]

def bfs(row,col,graph):
    global visited
    queue = deque()
    queue.append([row,col])
    visited[row][col]=True
    cnt_o=0
    cnt_v=0
    if farm_map[row][col]=='v':
        cnt_v+=1
    elif farm_map[row][col] == 'o':
        cnt_o += 1

    while(queue):
        r,c = queue.popleft()
        for child_r,child_c in graph[r][c]:
            if not visited[child_r][child_c]:
                queue.append([child_r,child_c])
                visited[child_r][child_c]=True
                if farm_map[child_r][child_c]=='v':
                    cnt_v+=1
                elif farm_map[child_r][child_c]=='o':
                    cnt_o+=1
    if cnt_o>cnt_v:
        return cnt_o,0
    else :
        return 0,cnt_v
total_o=0
total_v=0

for i in range(r):
    for j in range(c):
        if farm_map[i][j]!='#' and not visited[i][j]:
            o,v = bfs(i,j,graph)
            total_o+=o
            total_v+=v
print(total_o,total_v)



#그래프 없이 dx,dy를 child로 하면 되는데...