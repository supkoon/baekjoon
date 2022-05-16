import sys
from collections import deque

def bfs(start,end,graph):
    queue = deque()
    queue.append(start)
    visited = [0 for _ in range(len(graph))]
    parents = [0 for _ in range(len(graph))]
    visited[start]=True
    while(queue):
        expanded = queue.popleft()
        if expanded == end:
            break
        for child in graph[expanded]:
            if not visited[child]:
                visited[child]=True
                queue.append(child)
                parents[child]=expanded
    return parents
n = int(sys.stdin.readline())
p1,p2 = map(int,sys.stdin.readline().split())

m = int(sys.stdin.readline())
graph = [[] for p in range(n+1)]
for edge in range(m):
    start,end = map(int,sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

parents = bfs(p1,p2,graph)

start = p2
cnt=0
if parents[start]==0:
    print(-1)
else:
    while(start!=p1):
        start = parents[start]
        cnt+=1
    print(cnt)



