import heapq
import sys
m,n = map(int,sys.stdin.readline().split())

graph = []
for i in range(n):
    line = list(map(int,list(input())))
    graph.append(line)
dx = [-1,0,0,1]
dy = [0,1,-1,0]
INF = int(1e9)
distance = [[INF]*(m) for _ in range(n)]

def dijkstra(start):
    queue=list()
    heapq.heappush(queue,(0,[0,0]))
    distance[0][0]=0
    while(queue):
        dist,now = heapq.heappop(queue)
        for d in range(4):
            x_new,y_new = now[0]+dx[d],now[1]+dy[d]
            if 0<=x_new<n and 0<=y_new<m:
                cost = dist + graph[x_new][y_new]
                if cost < distance[x_new][y_new]:
                    distance[x_new][y_new]=cost
                    heapq.heappush(queue,[cost,[x_new,y_new]])

dijkstra([n-1,m-1])
print(distance[n-1][m-1])


