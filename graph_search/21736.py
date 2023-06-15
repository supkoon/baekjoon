'''
아이디어 
단순한 완전탐색 문제

그래프 초기화 과정에서 start 위치를 저장
완전탐색 

복잡도
O(N^2)

변수
start
graph
cnt
'''
from collections import deque
def bfs():
    queue = deque()
    queue.append(start)
    graph[start[0]][start[1]]='X'
    cnt=0
    while(queue):
        x,y = queue.popleft()
        for dx,dy in [[0,-1],[0,1],[-1,0],[1,0]]:
            nx = x+dx
            ny = y+dy
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]!='X':
                    queue.append([nx,ny])
                    if graph[nx][ny]=='P':
                        cnt+=1
                    graph[nx][ny]='X'
    if cnt==0:
        return 'TT'
    else : 
        return cnt

n,m = map(int,input().split())
graph = []
flag=True

for i in range(n):
    line = list(input())
    graph.append(line)
    if flag :
        for j in range(m):
            if graph[i][j]=='I':
                start = (i,j)
                flag=False       

print(bfs())


