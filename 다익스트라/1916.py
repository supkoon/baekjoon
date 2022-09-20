import sys
import heapq
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[]*(n+1) for _ in range(n+1)]
INF = int(1e9)
distance = [INF]*(n+1)
for i in range(m):
    start,end,weight = map(int,sys.stdin.readline().split())
    graph[start].append([end,weight])
s,e = map(int,sys.stdin.readline().split())

def dijkstra():
    global s,e,distance
    queue=list()
    distance[s]=0
    #우선순위 큐에 (거리, 노드)
    heapq.heappush(queue,(0,s))
    while(queue):
        dist,now = heapq.heappop(queue)
        if distance[now]<dist:
            continue

        for child in graph[now]:
            cost = dist+child[1]
            if cost < distance[child[0]]:
                distance[child[0]]=cost
                heapq.heappush(queue,(cost,child[0]))

dijkstra()
print(distance[e])