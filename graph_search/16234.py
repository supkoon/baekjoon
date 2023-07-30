'''
문제
인구이동

nxn의 땅이 있음. 

각 땅에는 하나의 나라가 존재. (1x1)
2차원 배열의 각 성분은 나라의 인구

하룻동안 다음과 같은 인구이동(인구이동이 없을떄까지 진행됨)

두 나라의 인구 차이가 L~R 사이면 국경선을 연다
--> 인구이동 시작
--> 이동 가능하면 두 나라는 하룻동안 연합
--> 연합을 이루는 나라으 ㅣ인구수는 연합인구/연합칸수가 된다.(소수점 버림)
--> 연합을 해체한다.  

며칠간 인구이동이 발생하는지 작성(모든 국경이 L~R 밖일떄까지 인듯)


아이디어



복잡도


'''

from collections import deque
import sys 
n,l,r = map(int,input().split())
graph = []

for i in range(n):
    line = list(map(int,sys.stdin.readline().split()))
    graph.append(line)

def iteration():
    global visited
    cnt = 0 
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                cnt += bfs(i,j)
    return cnt 

def bfs(i,j):
    global visited,graph,l,r
    queue = deque()
    queue.append([i,j])
    visited[i][j]=1
    people = graph[i][j]
    teams  = [[i,j]]
    
    while(queue):
        x,y = queue.popleft()
        for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
            nx,ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0 and l<=abs(graph[nx][ny]-graph[x][y])<=r:
                queue.append([nx,ny])
                visited[nx][ny]=1
                people += graph[nx][ny]
                teams.append([nx,ny])

    new_people = people//len(teams)
    for x,y in teams:
        graph[x][y] = new_people

    return len(teams)-1

cnt=0
while(True):
    #매번 그래프를 새로 만들어야할것 같음.
    # 아니다. 매 턴, 매 위치에서 전파를 시도한다, 이때 전파 조건을 L,R에 따라서.
    # 전파 횟수를 센다. 
    # 전파가 이루어지지 않았다면 flag를 바꾼다. 
    visited = [[0]*n for _ in range(n)]
    cnt_each = iteration()
    if not cnt_each:
        print(cnt)
        break  
    else:
        cnt+=1 