import sys
from collections import deque
n = int(sys.stdin.readline())
line = map(int,sys.stdin.readline().split())
graph  = [[] for node in range(n+1)]
for idx,n_jump in enumerate(line,start=1):
    for i in range(1,n_jump+1):
        next = idx+i
        if next <=n :
            graph[idx].append(next)
def bfs(start,graph):
    visited = [0 for node in range(len(graph))]
    path_count = [0 for node in range(len(graph))]
    queue = deque()
    queue.append(start)
    visited[start]=True
    while(queue):
        expanded = queue.popleft()
        for child in graph[expanded]:
            if not visited[child]:
                path_count[child] = path_count[expanded]+1
                visited[child]=True
                queue.append(child)
    return path_count,visited
path_count,visited = bfs(1,graph)

if n==1:
    print(0)
elif visited[n]:
    print(path_count[n])
else :
    print(-1)