import sys
from collections import deque

n,m, r= map(int,sys.stdin.readline().split())
graph  = [[] for node in range(n+1)]

for i in range(m):
    start,end = map(int,sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

def bfs(start,graph):
    visited = [0 for node in range(n+1)]
    queue= deque()
    queue.append(start)
    visited[start]=1
    while(queue):
        expanded = queue.popleft()
        for child in graph[expanded]:
            if not visited[child]:
                visited[child]=visited[expanded]+1
                queue.append(child)
    return visited

visited =bfs(r,graph)
for i in visited[1:]:
    if i==0:
        print(-1)
    else: print(i-1)





