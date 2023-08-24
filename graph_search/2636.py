'''
문제
치즈가 있음
공기와 접촉하면 한시간 뒤에 녹음
안에 구멍은 안녹는데, 구멍이 뚫리면 녹음
녹는데 걸리는 시간은?


아이디어
bfs
치즈 좌표에서 4방향 탐색
구멍이 뚫려야 녹는다는 것-->상하좌우만 본다는것

매 턴 시뮬레이션
치즈좌표에서 사방 탐색해서 하나라도 공기접촉하면 queue에 안넣기.

'''
import sys 
from collections import deque
n, m = map(int,input().split())
cheese = []
graph = []
for i in range(n):
    line = list(map(int,sys.stdin.readline().split()))
    graph.append(line)
moves = [(-1,0),(1,0),(0,1),(0,-1)]
before =0 

def bfs():
    global before 
    queue = deque()
    queue.append([0,0])
    visited = [[0]*m for _ in range(n)]
    visited[0][0]= 1
    melting_list = []
    while(queue):
        x,y = queue.popleft()
        for idx in range(4):
            nx, ny = x+moves[idx][0] , y+moves[idx][1]
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny]:
                    visited[nx][ny]=1
                    if graph[nx][ny]:
                        melting_list.append([nx,ny])
                    else:
                        queue.append([nx,ny])
    if not melting_list:
        return False
    else :
        for x,y in melting_list:
            graph[x][y] = 0
        before = len(melting_list)
        return True
    
cnt = 0 
while(True):
    if not bfs():
        print(cnt)
        print(before)
        break
    cnt+=1



    