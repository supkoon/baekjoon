def bfs(start_v):
    discovered =[start_v]
    queue = [start_v]
    while(queue):
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered
n= int(input())
m = int(input())
graph = dict()
for i in range(1,n+1):
    graph.setdefault(i,list())
for i in range(m):
    a,b = list(map(int,input().split()))
    graph[a].append(b)
    graph[b].append(a)
discovered = bfs(1)
print(len(discovered)-1)

