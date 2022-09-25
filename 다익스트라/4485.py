import heapq
import sys

results = []
dx =[-1,0,0,1]
dy =[0,-1,1,0]
def dijkstra(start,graph,distance):
    global dx,dy,n
    x,y=start[0],start[1]
    queue =list()
    heapq.heappush(queue,[graph[x][y],[x,y]])
    distance[x][y]=graph[x][y]
    while(queue):
        dist,now = heapq.heappop(queue)
        x,y = now[0],now[1]
        if dist>distance[now[0]][now[1]]:
            continue
        for d in range(4):
            x_new,y_new = +x+dx[d],y+dy[d]
            if 0<=x_new<n and 0<=y_new<n:
                cost = dist + graph[x_new][y_new]
                if cost<distance[x_new][y_new]:
                    distance[x_new][y_new]=cost
                    heapq.heappush(queue,[cost,[x_new,y_new]])

    return distance[n-1][n-1]

while(True):
    n = int(sys.stdin.readline())
    if not n:
        break
    graph = []
    INF = int(1e9)
    distance = [[INF]*n for _ in range(n)]
    for i in range(n):
        line = list(map(int,sys.stdin.readline().split()))
        graph.append(line)
    result = dijkstra([0,0],graph,distance)
    results.append(result)
for idx,i in enumerate(results,1):
    print(f'Problem {idx}: {i}')


