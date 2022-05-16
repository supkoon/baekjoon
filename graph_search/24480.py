import sys
sys.setrecursionlimit(1000000)
def dfs(start,graph,visited,path):
    global cnt
    visited[start]=True
    path[start] = cnt
    cnt += 1
    for child in sorted(graph[start],reverse=True):
        if not visited[child]:
            dfs(child,graph,visited,path)
    return path
#init
n,m,r = map(int,sys.stdin.readline().split())
graph =  [[] for node in range(n+1)]
visited = [0 for node in range(n+1)]
path = [0 for node in range(n+1)]
for edge in range(m):
    start,end = map(int,sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

cnt =1
path = dfs(r,graph,visited,path)
for i in path[1:]:
    print(i)
