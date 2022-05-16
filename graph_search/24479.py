import sys
sys.setrecursionlimit(100000)
n,m,r = map(int,sys.stdin.readline().split())

def dfs(start,graph):
  global cnt
  visited[start]=True
  if path[start]==0:
        path[start]=cnt
        cnt +=1
  for child in sorted(graph[start]):
    if not visited[child]:
      dfs(child,graph)
#init
graph = [[] for node in range(n+1)]
visited = [0 for node in range(n+1)]
path = [0 for node in range(n+1)]
for edge in range(m):
  start,end = map(int,sys.stdin.readline().split())
  graph[start].append(end)
  graph[end].append(start)

#dfs
cnt=1
dfs(r,graph)
for i in path[1:]:
  print(i)

