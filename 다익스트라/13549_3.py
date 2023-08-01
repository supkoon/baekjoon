'''
다익스트라 복습.
다익스트라 --> weighted edge이며 하나의 정점으로부터 다른 정점까지의 최단거리를 구함. 음의 간선일떄 불가능함. 

문제
수빈이는 숨바꼭질 진행중
걷는다면 1초 후 x-1,x+1
순간이동 0초후 2*x

가장 빠른 시간은?

아이디어
수빈이와 동생의 위치--> 하나의 정점으로부터 다른 하나의 정점(동생) 까지의 거리

'''
import heapq


n,k = map(int,input().split())
INF = 1e9
distance = [INF for _ in range(200001)]

def dijkstra(start):
    queue = []
    heapq.heappush(queue,[0,start])
    distance[start]=0

    while(queue):
        dist,node = heapq.heappop(queue)
        
        if distance[node] < dist:
            continue
        
        for idx,child in enumerate([node+1,node-1,2*node]):
            if 0<=child<=200000:
                cost = dist
                if idx !=2:
                    cost += 1
                if cost < distance[child]:
                    heapq.heappush(queue,[cost,child]) 
                    distance[child]=cost

dijkstra(n)
print(distance[k])
