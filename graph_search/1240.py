import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

def bfs(start,end,grpah):
    queue = deque()
    visited = [0 for _ in range(n+1)]
    queue.append(start)
    visited[start]=1
    while(queue):
        expanded = queue.popleft()
        for child,length in graph[expanded]:
            if not visited[child]:
                visited[child]=visited[expanded]+length
                if child == end:
                    return visited[child]
                else :
                    queue.append(child)

for case in range(n-1):
    start,end,length = map(int,sys.stdin.readline().split())
    graph[start].append([end,length])
    graph[end].append([start,length])

for case in range(m):
    start,end = map(int,sys.stdin.readline().split())
    print(bfs(start,end,graph)-1)

