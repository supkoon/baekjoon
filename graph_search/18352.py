# import sys
# from collections import deque
# n,m,k,x = map(int,sys.stdin.readline().split())
# graph = [[] for node in range(n+1)]
# visited = [0 for node in range(n+1)]
# path = [0 for node in range(n+1)]
# for edge in range(m):
#     start,end = map(int,sys.stdin.readline().split())
#     graph[start].append(end)
#
# def bfs(start,graph):
#     global visited
#     global path
#     queue = deque()
#     queue.append(start)
#     visited[start]=True
#     while(queue):
#         expanded = queue.popleft()
#         for child in graph[expanded]:
#             if not visited[child]:
#                 visited[child]=True
#                 queue.append(child)
#                 path[child]=path[expanded]+1
# bfs(x,graph)
# cnt=0
# for idx,node in enumerate(path):
#     if node==k:
#         print(idx)
#         cnt+=1
# if cnt==0:
#     print(-1)


