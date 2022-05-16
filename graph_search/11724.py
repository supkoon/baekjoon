import sys

def bfs(start,graph,visited):
    queue = [start]
    while queue:
        expanded = queue.pop(0)
        for child in graph[expanded]:
            if not visited[child]:
                queue.append(child)
                visited[child]=True

n, m  = map(int,sys.stdin.readline().split())
graph  = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
for case in range(m):
    start,end = map(int,sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

cnt = 0

for node in range(1,n+1):
    if not visited[node]:
        cnt+=1
        bfs(node,graph,visited)

print(cnt)


