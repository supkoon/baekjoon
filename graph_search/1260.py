from collections import deque
#deque : 양방향 큐 --> stack, queue 모두로 활용 가능 .
def bfs(graph, v, visited):
    queue = deque([v])
    visited[v]= True
    #없을떄까지 반복
    while(queue):
        #앞에서 하나 뽑음
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

def dfs(graph,v,visited):
    visited[v]=True
    print(v, end = ' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)


n,m,v = map(int,input().split())
graph = [[] for i in range(n+1)]
visited_dfs = [False]*(n+1)
visited_bfs = [False]*(n+1)

for case in range(m):
    i,j = list(map(int,input().split()))
    graph[i].append(j)
    graph[j].append(i)
for i in range(len(graph)):
    graph[i] = sorted(graph[i])
dfs(graph,v,visited_dfs)
print()
bfs(graph,v,visited_bfs)
