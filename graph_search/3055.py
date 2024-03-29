'''
문제
고슴도치가 비버의 굴로 들어가서 홍수를 피하려고함.

비어있는 곳 : . 
물 : *
돌 : X
비버굴 : D
시작지점 : S

사방으로 이동가능
물은 비어있는 칸으로 확장됨.
물, 고슴도치는 돌 통과 못함
도착지점으로도 물 못감

물이 찰 예정인 곳으로도 이동할 수 없음.


비버굴로 가기위한 최소시간

아이디어:
시뮬레이션, bfs

매 턴이 진행
매 턴마다 물이 이동함. 

전하게 비버의 굴로 이동할 수 없다면, "KAKTUS" 출력 

'''
import sys 
from collections import deque
import copy

r, c = map(int,sys.stdin.readline().split())


graph = []
for i in range(r):
    line = list(sys.stdin.readline().rstrip())
    for j in range(c):
        if line[j]=='S':
            start = (i,j)
        elif line[j]=='D':
            end = (i,j)
    graph.append(line)
    

def move_water():
    new_water = []
    for x in range(r):
        for y in range(c):
            if graph[x][y]=='*':
                for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                    nx,ny = x+dx, y +dy
                    if 0<=nx<r and 0<=ny<c and graph[nx][ny] not in ['D','X']:
                        new_water.append((nx,ny))
    for x, y in new_water:
        graph[x][y] = '*'              


visited = [[0] * c for _ in range(r)]

minutes = 1
def bfs():
    global graph, minutes
    now_x,now_y = start 
    queue = deque()
    queue.append((now_x,now_y))
    visited[now_x][now_y] =  1

    
    while(queue):
        x,y = queue.popleft()

        if minutes <= visited[x][y]:
            move_water()
            minutes+=1

        
        for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
            nx,ny = x+dx, y +dy
            
            if 0<=nx<r and 0<=ny<c and graph[nx][ny] not in ['*','X']:
                if not visited[nx][ny]:
                    queue.append((nx,ny))
                    visited[nx][ny] = visited[x][y]+1
        
bfs()

if visited[end[0]][end[1]]:
    print(visited[end[0]][end[1]]-1)
else:
    print('KAKTUS')