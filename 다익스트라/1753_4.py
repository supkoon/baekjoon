'''
다익스트라 복습 




'''
import sys
import heapq

v,e = map(int,sys.stdin.readline().split())
start = int(input())
INF = 1e9
distance = [INF for _ in range(v+1)]

graph = [[] for _ in range(v+1)]

for edge in range(e):
    s,e,w = map(int,sys.stdin.readline().split())
    graph[s].append([w,e])

def dijkstra(start):
    queue = list()
    heapq.heappush(queue,[0,start])
    distance[start] = 0 

    while(queue):
        dist,now = heapq.heappop(queue)
        if distance[now] < dist:
            continue

        for dist_child,child in graph[now]:
            if distance[child] > dist + dist_child:
                 distance[child] = dist + dist_child
                 heapq.heappush(queue,[dist_child + dist, child])
dijkstra(start)

for i in distance[1:]:
    if i ==INF:
        print('INF')
    else:
        print(i)