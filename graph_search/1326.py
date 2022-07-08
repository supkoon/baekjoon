import sys
from collections import deque
n = int(sys.stdin.readline())
n_jumps = list(map(int,sys.stdin.readline().split()))
graph = [[] for node in range(n+1)]
start,end = map(int,sys.stdin.readline().split())

# for node in range(1,n+1):
#     can_jump = list(range(node,end+1,n_jumps[node-1]))
#     for i in can_jump:
#         graph[node].append(i)
#     can_jump = list(range(node,-1,-n_jumps[node-1]))
#     for i in can_jump:
#         if i not in graph[node]:
#             graph[node].append(i)
def bfs(start,end,graph):
    queue = deque()
    queue.append(start)
    visited = [0 for node in range(len(graph))]
    while(queue):
        expanded = queue.popleft()
        for child in range(expanded,n+1,n_jumps[expanded-1]):
            if not visited[child]:
                visited[child] = visited[expanded] + 1
                if child==end:
                    print(visited[child]-1)
                    break
                else :
                    queue.append(child)
        for child in range(expanded, -1, -n_jumps[expanded - 1]):
            if not visited[child]:
                visited[child] = visited[expanded] + 1
                if child == end:
                    print(visited[child] - 1)
                    break
                else:
                    queue.append(child)
    if not visited[end-1]:
        print(-1)
bfs(start,end,graph)

