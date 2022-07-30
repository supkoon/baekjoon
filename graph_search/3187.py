from collections import deque
r,c = map(int,input().split())

graph = [list(input()) for _ in range(r)]
dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]
visited = [[0] * c for _ in range(r)]

def bfs(i,j,graph):
    global dx,dy, visited
    queue=deque()
    queue.append([i,j])
    visited[i][j]=1
    num_v = 0
    num_k = 0
    if graph[i][j]=='k':
        num_k+=1
    elif graph[i][j]=='v':
        num_v+=1

    while(queue):
        i,j = queue.popleft()
        for d in range(4):
            new_i = i+dx[d]
            new_j = j+dy[d]
            if 0<=new_i<r and 0<=new_j<c and not visited[new_i][new_j]:
                if graph[new_i][new_j] !='#':
                    visited[new_i][new_j]=1
                    queue.append([new_i,new_j])
                    if graph[new_i][new_j]=='v':
                        num_v+=1
                    elif graph[new_i][new_j]=='k':
                        num_k+=1
    return num_v,num_k

total_v=0
total_k=0
for i in range(r):
    for j in range(c):
        if not visited[i][j]:
            num_v,num_k = bfs(i,j,graph)
            if num_v>=num_k:
                total_v+=num_v
            else:
                total_k+=num_k
print(total_k,total_v)


