from collections import deque
n = int(input())
graph = [[] for _ in range(n)]
starts = []
for i in range(n):
    line = list(map(int,input().split()))
    for j in range(n):
        if line[j]==1:
            starts.append(i)
            graph[i].append(j)
global_visited=[[0]*n for _ in range(n)]

def bfs(start,graph):
    global global_visited
    visited = [0 for _ in range(n)]
    queue= deque()
    queue.append(start)
    while(queue):
        expanded = queue.popleft()
        for child in graph[expanded]:
            if not visited[child]:
                queue.append(child)
                visited[child]=1
                global_visited[start][child]=1
for i in starts:
    bfs(i,graph)
for i in global_visited:
    for j in i:
        print(j,end=' ')
    print()