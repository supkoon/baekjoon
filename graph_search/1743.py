'''
문제

음식물은 서로 뭉침

떨어진 음식물 중에 제일 큰 음식물만은 피해 가려고 한다. 

선생님을 도와 제일 큰 음식물의 크기를 구해서 “10ra"를 외치지 않게 도와주자.



도로 길이 n,m
음식물 쓰레기 수 k
k개의 좌표 r,c


아이디어
각 음식물에서 시작하여 완전탐색.
각 위치에서 bfs 실행해서 크기 return 받고, 전체 경우에서 max 구해서 리턴.



복잡도
log(n^2)

변수
n,m,k
graph
trash
visited


'''
import sys
from collections import deque
n,m,k = map(int,sys.stdin.readline().split())
graph = [[0]*m for _ in range(n)]


trash = []
for i in range(k):
    x,y = map(int,sys.stdin.readline().split())
    graph[x-1][y-1]=1
    trash.append((x-1,y-1))


def bfs(x,y):
    visited = [[0]*m for _ in range(n)]
    queue = deque()
    queue.append([x,y])
    visited[x][y]=1
    cnt = 1
    while(queue):
        x,y = queue.popleft()
        for dx,dy in [(-1,0),(0,-1),(0,1),(1,0)]:
            nx,ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and graph[nx][ny]:
                    visited[nx][ny]=1
                    cnt+=1
                    queue.append((nx,ny))

    return cnt

max_cnt = -1e10


for x,y in trash:
    cnt = bfs(x,y)
    max_cnt = max(max_cnt,cnt)

print(max_cnt)




