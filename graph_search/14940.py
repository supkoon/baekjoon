'''
아이디어
지도n,m
0 x
1 길
2 목표
각 지점에서 목표까지 거리

그래프 초기화를 -2씩함.  
목표지점에서 시작하여 bfs로 완전탐색. 
원래 못가는 땅은 0 줌


복잡도
bfs 1회 실행 O(n^2)

변수
n,m
graph
'''

from collections import deque
n,m = map(int,input().split())

graph = []

for i in range(n):
    line = list(map(int,input().split()))
    for j in range(m):
        if line[j]==2:
            start = (i,j)
        if line[j]!=0:
            line[j]-=2
        
    graph.append(line)
     
            
def bfs():
    queue = deque()
    queue.append([start[0],start[1]])
    while(queue):
        x,y = queue.popleft()
        for dx,dy in [[0,-1],[0,1],[1,0],[-1,0]]:
            nx = x+dx
            ny = y+dy
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]== -1:
                    queue.append([nx,ny])
                    graph[nx][ny]=graph[x][y]+1
                
bfs()
for i in graph:
    for j in i:
        print(j,end=' ')
    print()

