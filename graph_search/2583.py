import sys
from collections import deque
m,n,k = map(int,sys.stdin.readline().split())
graph = [[0]*n for _ in range(m)]
for case in range(k):
    #0 2 4 4
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    for x in range(x1,x2):
        for y in range(y1,y2):
            graph[y][x]=-1
def bfs(i,j,grpah):
    queue= deque()
    queue.append([i,j])
    graph[i][j]=1
    cnt = 0
    while(queue):
        expanded_i,expanded_j = queue.popleft()
        for dx,dy in [[-1,0],[1,0],[0,1],[0,-1]]:
            new_i,new_j = expanded_i+dx,expanded_j+dy
            if 0<=new_i<m and 0<=new_j<n:
                if graph[new_i][new_j]==0:
                    queue.append([new_i,new_j])
                    graph[new_i][new_j]=1
                    cnt+=1
    return cnt

results = []
for i in range(m):
    for j in range(n):
        if graph[i][j]==0:
            cnt = bfs(i,j,graph)
            results.append(cnt+1)
print(len(results))
print(' '.join(map(str,sorted(results))))
