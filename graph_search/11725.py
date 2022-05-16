import sys
from collections import deque

def bfs(start,graph):
    queue = deque()
    queue.append(start)
    visited = [0 for _ in range(n+1)]
    parents = [0 for _ in range(n+1)]
    while(queue):
        expanded =queue.popleft()
        for child in graph[expanded]:
            if not visited[child]:
                visited[child]=True
                queue.append(child)
                parents[child] = expanded
    return parents

n = int(sys.stdin.readline())
graph  = [[] for node in range(n+1)] # 0~n

for edge in range(n-1):
    start, end = map(int,sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

parents = bfs(1,graph)

for i in parents[2:]:
    sys.stdout.write(str(i)+'\n')



