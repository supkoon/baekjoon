import sys
from collections import deque
from itertools import combinations
import copy
n,m = map(int,sys.stdin.readline().split())
graph = []
virus = []
empty = []
for i in range(n):
    line = list(map(int,input().split()))
    for j in range(m):
        if line[j]==2:
            virus.append([i,j])
        elif line[j]==0:
            empty.append([i,j])
    graph.append(line)

dx = [-1,0,0,1]
dy = [0,-1,1,0]

def bfs(tmp):
    global dx,dy
    queue=deque()
    visited = [[0]*m for _ in range(n)]
    for i,j in virus:
        visited[i][j]=1
        queue.append([i, j])
    while(queue):
        length = len(queue)
        for i in range(length):
            x,y = queue.popleft()
            for d in range(4):
                new_x,new_y = x+dx[d],y+dy[d]
                if 0<=new_x<n and 0<=new_y<m:
                    if tmp[new_x][new_y]!=1 and not visited[new_x][new_y]:
                        queue.append([new_x,new_y])
                        visited[new_x][new_y]=1
                        tmp[new_x][new_y]=2
            #each virus point


cnt_max=0
for wall_1,wall_2,wall_3 in combinations(empty,3):
    tmp = copy.deepcopy(graph)
    #Each case 벽세우기
    tmp[wall_1[0]][wall_1[1]] = 1
    tmp[wall_2[0]][wall_2[1]] = 1
    tmp[wall_3[0]][wall_3[1]] = 1
    cnt=0
    bfs(tmp)

    for i in tmp:
        for j in i:
            if j==0:
                cnt+=1
    if cnt_max<cnt:
        cnt_max=cnt

print(cnt_max)


