import heapq
import sys
n,e = map(int,sys.stdin.readline().split())
graph = [[]*(n+1) for _ in range(n+1)]
for i in range(e):
    s,e,w = map(int,sys.stdin.readline().split())
    graph[s].append([e,w])
    graph[e].append([s,w])
p1,p2 = map(int,sys.stdin.readline().split())
INF = int(1e9)
def dijkstra(start,distance):
    queue=list()
    heapq.heappush(queue,[0,start])
    distance[start]=0
    while(queue):
        dist,now =heapq.heappop(queue)
        if distance[now]<dist:
            continue
        for child in graph[now]:
            cost= dist+child[1]
            if cost<distance[child[0]]:
                distance[child[0]]=cost
                heapq.heappush(queue,[cost,child[0]])
start = 1
end = n
total1,total2 = 0,0
distance = [INF for _ in range(n+1)]
dijkstra(start,distance)
total1 += distance[p1]
total2 += distance[p2]
distance1 = [INF for _ in range(n+1)]
distance2 = [INF for _ in range(n+1)]
dijkstra(p1,distance1)
dijkstra(p2,distance2)
total1 += distance1[p2]+distance2[n]
total2 += distance2[p1]+distance1[n]
result = min(total1,total2)
if result>=INF:
    print(-1)
else:
    print(result)


