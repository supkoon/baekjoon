import heapq
import sys
n,m,r = map(int,sys.stdin.readline().split())
#총합이 M 이하
items = [0]+list(map(int,sys.stdin.readline().split()))
graph = [[] for _ in range(n+1)]
for i in range(r):
    s,e,w = map(int,sys.stdin.readline().split())
    graph[s].append([e,w])
    graph[e].append([s,w])
INF = int(1e9)
def dijkstra(start):
    global graph,m,items
    distance = [INF] * (n + 1)
    queue=list()
    heapq.heappush(queue,[0,start])
    distance[start]=0

    while(queue):
        dist,now = heapq.heappop(queue)
        if distance[now]<dist:
            continue
        for child in graph[now]:
            cost= dist+child[1]
            if cost<=m and cost < distance[child[0]]:
                heapq.heappush(queue,[cost,child[0]])
                distance[child[0]]=cost
    total = 0
    for i in range(1,n+1):
        if distance[i] <INF :
            total+=items[i]
    return total
result=0
for i in range(1,n+1):
    num= dijkstra(i)
    if result < num:
        result = num
print(result)





