import sys
r,c  = map(int,sys.stdin.readline().split())
graph = []
for i in range(r):
    line = sys.stdin.readline().rstrip()
    graph.append(line)
dx = [0,-1,1,0]
dy = [-1,0,0,1]
def bfs():
    global graph
    cnt=1
    queue = set([(0, 0, graph[0][0])])
    while(queue):
        x,y,alpha=queue.pop()
        for d in range(4):
            x_new,y_new = x+dx[d],y+dy[d]
            if 0<=x_new<r and 0<=y_new<c and graph[x_new][y_new] not in alpha:
                    queue.add((x_new,y_new,alpha+graph[x_new][y_new]))
                    cnt = max(cnt,len(alpha)+1)
    return cnt
print(bfs())

#dfs로 해야할거같음.