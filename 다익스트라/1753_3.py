'''
다익스트라 복습
weighted edge인 경우에 최단경로를 찾을때 다익스트라를 써야함.
플로이드워셜은 아직 모름 ㅎㅎ

문제
정점 수, 간선 수 v e 

아이디어
다익스트라

복잡도
O(n^2)

'''
import sys 
import heapq
v,e = map(int,input().split())
start = int(input())
graph = [[] for _ in range(v+1)] # 0 제외
INF = 1e10
distance = [INF for _ in range(v+1)]

for edge in range(e):
    s,e,w = map(int, sys.stdin.readline().split())
    graph[s].append([e,w]) #edge,weight 형태로 추가

def dijkstra(start):
    queue = []
    heapq.heappush(queue,[0,start])
    distance[start] = 0 

    while(queue):
        dist,node = heapq.heappop(queue)
        if dist > distance[node]:
            continue #해당 노드는 이미 업데이트 됐음

        for child, dist_child in graph[node]:
            if dist + dist_child < distance[child]:
                distance[child] = dist + dist_child
                heapq.heappush(queue,[distance[child],child])

dijkstra(start)

for i in distance[1:]:
    if i == INF:
        print('INF')
    else:
        print(i)

