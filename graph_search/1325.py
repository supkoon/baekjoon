from collections import deque
import sys
n,m = map(int,input().split())
graph =  [[] for node in range(n+1)]
for edge in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[b].append(a)
def bfs(start,graph):
    cnt=1
    queue = deque()
    queue.append(start)
    visited = [0 for node in range(n+1)]
    visited[start]=True
    while(queue):
        expanded = queue.popleft()
        for child in graph[expanded]:
            if not visited[child]:
                visited[child]=True
                queue.append(child)
                cnt+=1
    return cnt
result = []
max_visited = -1
for node in range(1,n+1):
    cnt = bfs(node,graph)
    if cnt>max_visited:
        max_visited=cnt
        result= [node]
    elif cnt==max_visited:
        result.append(node)
for node in sorted(result):
    print(node,end = " ")
