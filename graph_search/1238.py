'''
문제
n개의 마을에 각각 한명씩 삼
n명이 X마을에 모여서 파티
m개의 단방향 도로, t의 시간

파티가 끝나고 돌아와야함.(단방향 조심)

N명의 학생들 중 오고 가는데 가장 많은 시간을 쓴 사람은?


아이디어
1.모든 점에서 다른 점까지의 최단거리 --> 플로이드 워셜?
플로이드 워셜을 해놓고,
각 점에대해서 a->b + b->a 의 최소값을 해보자 . 
--> 시간초과(O(n^3))

혹은 다익스트라 1(시작 : x) + n-1번(시작 : 나머지)
우선순위 큐를 사용하는 다익스트라는 ElogE 라고함. 

2.
복잡도
 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 10,000), 

 
'''
import sys 
import heapq

n,m,x = map(int,sys.stdin.readline().split())
#x 파티장소
INF = 1e10
distance = [INF for _ in range(n+1)]
distance2 = [INF for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
graph2 = [[] for _ in range(n+1)]

for i in range(m):
    s,e,w = map(int,sys.stdin.readline().split())
    graph[s].append([w,e])
    graph2[e].append([w,s])

def dijkstra(start,graph,distance):
    queue = list()
    heapq.heappush(queue,[0,start])
    distance[start] = 0

    while(queue):
        dist,expanded = heapq.heappop(queue)
        if distance[expanded] < dist:
            continue

        for cost,child in graph[expanded]:
            if cost+dist < distance[child]:
                heapq.heappush(queue,[cost+dist,child])
                distance[child] = cost+dist
    return distance

distance = dijkstra(x,graph,distance)
distance2 = dijkstra(x,graph2,distance2)


result_max = 0
for node in range(1,n+1):
    if distance[node] + distance2[node] > result_max :
        result_max = distance[node] + distance2[node]
print(result_max)

