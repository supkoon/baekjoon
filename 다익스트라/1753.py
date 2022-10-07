import sys
import heapq
n,m = map(int,sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[]*(n+1) for _ in range(n+1)]
distance = [int(1e9)]*(n+1)
for i in range(m):
    u,v,w  = map(int,sys.stdin.readline().split())
    graph[u].append((v,w))

def dijkstra(start):
    global distance
    #우선순위 큐
    queue= []
    #heapq : heapq연산해주는 모듈
    heapq.heappush(queue,(0,start))
    #자신과의 거리는 0
    distance[start]=0

    while(queue):
        #heapq에서 가장 우선순위가 높은 원소가 나옴.
        dist,now = heapq.heappop(queue)
        #해당 노드의 현재 거리값이 나온것보다 이미 좋으면 이미 업데이트 된걸로 치고 패스
        if distance[now]<dist:
            continue
        #자식노드
        for child in graph[now]:
            #기존 + 자식까지의 거리
            cost = dist+child[1]
            #그게 현재 자식노드가 가진 거리보다 작으면? -->  갱신
            if cost < distance[child[0]]:
                distance[child[0]] = cost
                heapq.heappush(queue,(cost,child[0]))

dijkstra(start)

for i in distance[1:]:
    if i==int(1e9):
        print("INF")
    else:   print(i)
