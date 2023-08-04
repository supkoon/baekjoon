'''
문제
하나의 정점에서 다른 모든 정점으로까지의 최단거리

아이디어
다익스트라

'''

import sys 
import heapq
v,e = map(int,sys.stdin.readline().split())
start = int(input())
INF = 1e10
distance  = [INF for _ in range(v+1)]

graph = [[] for _ in range(v+1)]

for i in range(e):
    s,e,w = map(int,sys.stdin.readline().split())
    graph[s].append([w,e])

def dijkstra(start):
    queue = list()
    heapq.heappush(queue,[0,start])
    distance[start]=0

    while(queue):
        dist,node = heapq.heappop(queue)
        if dist > distance[node]:
            continue
        for cost,child in graph[node]:
            if cost+dist < distance[child]:
                distance[child] = cost+dist
                heapq.heappush(queue,[distance[child],child])

dijkstra(start)

for dist in distance[1:]:
    if dist!=INF:
        print(dist)
    else:
        print('INF')

