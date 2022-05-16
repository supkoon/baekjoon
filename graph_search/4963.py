import sys
dx = [0,0,1,1,1,-1,-1,-1]
dy = [1,-1,1,0,-1,1,0,-1]


def bfs(a,b,graph):
    queue = [[a,b]]
    while queue:
        d1,d2 = queue[0][0], queue[0][1]
        queue.pop(0)
        for i in range(len(dx)):
            d1_ = d1+dx[i]
            d2_ = d2+dy[i]
            if 0<=d1_<len(graph) and 0<=d2_<len(graph[0]) and graph[d1_][d2_]:
                graph[d1_][d2_]=0
                queue.append([d1_,d2_])
while(True):
    d2,d1 = map(int,sys.stdin.readline().split())
    if d2==d1==0:
        break
    graph =  [list(map(int,sys.stdin.readline().split())) for _ in range(d1)]
    cnt = 0
    for d1_ in range(d1):
        for d2_ in range(d2):
            if graph[d1_][d2_]:
                cnt+=1
                bfs(d1_,d2_,graph)
    print(cnt)





