import heapq
import sys
n = int(sys.stdin.readline().rstrip())

#graph = [list(map(int,list(sys.stdin.readline().rstrip()))) for _ in range(n)]
graph = []
for i in range(n):
    line = list(map(int,list(sys.stdin.readline().rstrip())))
    line = map(lambda x : 1 if not x else 0, line)
    graph.append(list(line))
INF = int(1e9)
distance = [[INF]*n for _ in range(n)]
dx = [-1,0,0,1]
dy = [0,-1,1,0]
cnt=0
def dijkstra():
    global graph
    global cnt
    queue = list()
    heapq.heappush(queue,[0,[0,0]])
    while(queue):
        dist,now = heapq.heappop(queue)
        if distance[now[0]][now[1]] < dist:
            continue
        for d in range(4):
            x= now[0]+dx[d]
            y= now[1]+dy[d]
            if 0<=x<n and 0<=y<n:
                cost = graph[x][y]+dist
                if cost<distance[x][y]:
                    distance[x][y]=cost
                    heapq.heappush(queue,[cost,[x,y]])
dijkstra()
print(distance[n-1][n-1])