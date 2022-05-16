import sys
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(d1,d2,graph):
    queue = [[d1,d2]]
    while(queue):
        a, b = queue[0][0] , queue[0][1] #d1,d2
        queue.pop(0)
        for i in range(4):
            d1 = a+dx[i]
            d2 = b+dy[i]
            if 0 <= d1 < n and 0 <= d2 < m and graph[d1][d2]:
                graph[d1][d2] = 0
                queue.append([d1,d2])

n = int(sys.stdin.readline())

for case in range(n):
    m,n,k = map(int,sys.stdin.readline().split())
    #init
    graph = [[0]*m for _ in range(n)]
    cnt = 0
    for i in range(k):
        a,b = map(int,sys.stdin.readline().split())
        graph[b][a]=1

    #bfs
    for d1 in range(n):
        for d2 in range(m):
            if graph[d1][d2]:
                graph[d1][d2]=0
                bfs(d1,d2,graph)
                cnt+=1
    print(cnt)











