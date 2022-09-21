import heapq
n,m = map(int,input().split())
INF = int(1e9)
distance = [INF]*200001
def dijkstra(start):
    queue = []
    distance[start]=0
    heapq.heappush(queue,[0,start])
    while(queue):
        dist,now = heapq.heappop(queue)
        if distance[now]<dist:
            continue
        for idx,child in enumerate([now+1,now-1,2*now]):
            if 0<=child<=200000:
                cost = dist
                if idx !=2:
                    cost += 1
                if cost<distance[child]:
                    distance[child]=cost
                    heapq.heappush(queue,[cost,child])
dijkstra(n)
print(distance[m])




