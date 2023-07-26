'''
다익스트라 복습

문제
방향그래프가 주어졌을 때, 시작점에서 다른 정점으로의 최단경로

아이디어


복잡도 



'''

import sys
import heapq
n,m = map(int,input().split())
start = int(input())
INF = 1e9
distance = [INF for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for i in range(m):
    s,e,dist = map(int,sys.stdin.readline().split())
    graph[s].append([e,dist])

def dijkstra(start):
    queue = []
    heapq.heappush(queue,[0,start])
    distance[start] = 0 

    while(queue):
        dist,now = heapq.heappop(queue) #dist, node 
 
        if distance[now] < dist:
            continue
        #현재 노드까지의 거리를 뽑아보니, 이미 더 작은값이 저장되어 있으면, 다른 노드에서 처리해서 넣어놓은 것. (heapq엔 더 높은 값이 쌓여서 처리 안됐을 수도 있지만, distance는 계속 변경중ㅇ)

        for child in graph[now] : #end,cost
            cost = dist + child[1]
            if cost < distance[child[0]]:
                distance[child[0]] = cost
                heapq.heappush(queue,[cost,child[0]])


dijkstra(start)

for i in distance[1:]:
    if i==INF:
        print('INF',' ')
    else:
        print(i,end = ' ')
