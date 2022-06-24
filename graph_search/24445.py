import sys
from collections import deque
n,m,r = map(int,sys.stdin.readline().split())
graph = [[] for node in range(n+1)]

for node in range(m):
    start,end = map(int,sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)
#내림차순,오름차순 등으로 방문해야하면, 미리 sort를 하는것도 좋다.
#참고로 .sort()는 inplace !!!


def bfs(start,graph):
    queue = deque()
    queue.append(start)
    visited = [0 for node in range(n+1)]
    cnt=1
    visited[start]=cnt
    while(queue):
        expanded = queue.popleft()
        for child in sorted(graph[expanded],reverse=True):
            if not visited[child]:
                cnt+=1
                visited[child]=cnt
                queue.append(child)
    return visited

visited = bfs(r,graph)

for i in visited[1:]:
    sys.stdout.write(str(i)+"\n")
