from collections import deque
m,n,h = map(int,input().split())
graph = []
for box in range(h):
    graph.append([list(map(int,input().split())) for _ in range(n)])
visited = [[[0]*m for _ in range(n)] for _ in range(h)]
starts=[]
cnt_tomato_left=0 #남은 토마토 수
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k]==1:
                #익은 토마토 위치, visited True로 미리 설정
                starts.append([i,j,k])
                visited[i][j][k]=1
            elif graph[i][j][k]==0:
                cnt_tomato_left+=1
#시도해보려는것, --> 1로된거 다 queue에 넣고, 3차원행렬로 도전,
# 이거 안되면 +n -n(세로) 도전
#다 익으면 일수, 다 못익으면 -1

#좌,뒤,앞,우,상,하
dx = [-1,0,0,1,0,0]
dy = [0,-1,1,0,0,0]
dz = [0,0,0,0,-1,1]
time =0
flag=False
def bfs(starts,graph):
    global time,visited,dx,dy,dz,cnt_tomato_left
    queue=deque()
    for tomato in starts:
        queue.append(tomato)
    while(queue):
        if cnt_tomato_left == 0:
            break
        length = len(queue)
        time+=1
        for case in range(length):
            #h,n,m
            i,j,k = queue.popleft()
            for d in range(6):
                i_new,j_new,k_new = i+dz[d],j+dy[d],k+dx[d]
                if 0<=i_new<h and 0<=j_new<n and 0<=k_new<m:
                    if not visited[i_new][j_new][k_new] and graph[i_new][j_new][k_new]!=-1:
                        queue.append([i_new,j_new,k_new])
                        visited[i_new][j_new][k_new]=1
                        if graph[i_new][j_new][k_new]==0:
                            cnt_tomato_left-=1
                            graph[i_new][j_new][k_new]=1

bfs(starts,graph)
if cnt_tomato_left:
    print(-1)
else:
    print(time)
