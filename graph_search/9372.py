import sys
from collections import deque
def bfs(start,graph):
    visited = [0 for _ in range(len(graph))]
    queue = deque()
    queue.append(start)
    visited[start]=True
    cnt=0
    while(queue):
        expanded = queue.popleft()
        for child in graph[expanded]:
            if not visited[child]:
                cnt += 1
                visited[child]=True
                queue.append(child)

    return cnt

t = int(sys.stdin.readline())

for case in range(t):
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for country in range(n+1)]
    for edge in range(m):
        country_1, country_2 = map(int,sys.stdin.readline().split())
        graph[country_1].append(country_2)
        graph[country_2].append(country_1)
    cnt = bfs(1,graph)
    print(cnt)

