import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())
graph = [[] for node in range(n+1)]
for i in range(m):
    tall,small = map(int,sys.stdin.readline().split())
    graph[tall].append(small)
p,q = map(int,sys.stdin.readline().split())
def bfs(start,end,graph):
    queue = deque()
    queue.append(start)
    visited = [0 for node in range(n + 1)]
    visited[start]=True
    while(queue):
        expanded = queue.popleft()
        for child in graph[expanded]:
            if not visited[child]:
                visited[child]=True
                queue.append(child)
    if visited[end]:
        return True
    else :
        return False

taller_p = bfs(p,q,graph)
taller_q = bfs(q,p,graph)
if taller_p:
    print("yes")
elif taller_q:
    print("no")
else:
    print("unknown")






