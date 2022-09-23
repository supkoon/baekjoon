import heapq
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]

for i in range(m):
    s,e,w = map(int,sys.stdin.readline().split())
    graph[s].append([e,w])
start,end = map(int,sys.stdin.readline().split())
INF = int(1e9)

distance = [INF]*(n+1)

visited = [[] for _ in range(n+1)]
visited[start].append(start)

def dijkstra(start):
    global visited,distance
    queue=list()
    heapq.heappush(queue,[0,start])

    while(queue):
        dist,now = heapq.heappop(queue)
        if dist > distance[now]:
            continue
        if now == start:
            distance[now]=0
        for next,next_cost in graph[now]:
            cost = dist + next_cost
            if cost < distance[next]:
                distance[next]=cost
                visited[next]=visited[now]+[next]
                heapq.heappush(queue,[cost,next])

dijkstra(start)
print(distance[end])
print(len(visited[end]))
for i in visited[end]:
    print(i,end=' ')
