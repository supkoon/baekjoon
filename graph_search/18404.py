from collections import deque
import sys
n,m = map(int,sys.stdin.readline().split())
start_x,start_y = map(int,sys.stdin.readline().split())
enemies = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]
cnt = m
dx = [-2,-2,-1,-1,1,1,2,2]
dy = [-1,+1,2,-2,2,-2,1,-1]

def bfs(i,j):
    global cnt
    queue = deque()
    visited = [[0]*n for _ in range(n)]
    queue.append([i,j])
    visited[i][j]=1
    while(queue):
        x,y = queue.popleft()
        for move in range(8):
            new_x = x+dx[move]
            new_y = y+dy[move]
            if 0<=new_x<n and 0<=new_y<n:
                if not visited[new_x][new_y]:
                    visited[new_x][new_y]=visited[x][y]+1
                    queue.append([new_x,new_y])

visited = bfs(start_x-1,start_y-1)
for i,j in enemies:
    print(visited[i-1][j-1]-1,end=' ')






