import sys
sys.setrecursionlimit(1000000)
#init
n,m,r = map(int,sys.stdin.readline().split())
graph = [[] for node in range(n+1)]
for edge in range(m):
    start,end = map(int,sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)
visited = [0 for node in range(n+1)]
path = [0 for node in range(n+1)]
cnt=0
def dfs(start,graph):
    global cnt
    global path
    global visited
    visited[start]=True
    cnt+=1
    path[start]=cnt
    for child in sorted(graph[start],reverse=True):
        if not visited[child]:
            dfs(child,graph)
dfs(r,graph)
for node in path[1:]:
    print(node)





