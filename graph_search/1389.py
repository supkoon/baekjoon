import sys
from collections import deque
#graph init
n,m = map(int,sys.stdin.readline().split())
graph = [[] for node in range(n+1)]
for edge in range(m):
    start,end = map(int,sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

#bfs
def bfs(start,graph):
    queue= deque()
    queue.append(start)
    visited = [0 for node in range(len(graph))]
    path_cnt =[0 for node in range(len(graph))]
    visited[start]=True
    while(queue):
        expanded = queue.popleft()
        for child in graph[expanded]:
            if not visited[child]:
                visited[child]=True
                path_cnt[child]=path_cnt[expanded]+1
                queue.append(child)
    return path_cnt
min=10*6
ans=0
for node in range(1,n+1):
    path_cnt =bfs(node,graph)
    result = sum(path_cnt)
    if result<min:
        min = result
        ans = node
sys.stdout.write(str(ans))
