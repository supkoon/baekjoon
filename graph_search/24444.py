import sys
from collections import deque
#init
n,m,r = map(int,sys.stdin.readline().split())
graph = [[] for node in range(n+1)]
visited = [0 for node in range(n+1)]
path = [0 for node in range(n+1)]

for edge in range(m):
    start,end = map(int,sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)
cnt = 0
def bfs(start,graph):
    #변경할 변수는 전역처리
    global cnt
    global path
    global visited
    queue = deque()
    queue.append(start)
    visited[start]=True
    cnt+=1
    path[start]=cnt
    while(queue):
        expanded = queue.popleft()
        for child in sorted(graph[expanded]):
            if not visited[child]:
                queue.append(child)
                visited[child]=True
                cnt+=1
                path[child]=cnt

bfs(r,graph)
for i in path[1:]:
    print(i)