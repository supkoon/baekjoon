'''
문제
숫자 정사각형
직사각형에서 꼭짓점에 쓰인 수가 모두 같은 가장 큰 정사각형 찾기 

아이디어
각 위치를 기준으로 나머지 세점을 될때까지 시도 

복잡도
O(n^3)

변수
n,m
cnt 각 경우에서 네 점을 만족했는지. 
result : 결과

'''
n,m = map(int,input().split())
graph = []

for i in range(n):
    line = list(input())
    graph.append(line)

result = 0
for x in range(n):
    for y in range(m):
        for d in range(1,n):
            cnt = 0 
            for dx,dy in [[0,d],[d,0],[d,d]]:
                nx = x + dx
                ny = y + dy
                if 0<=nx<n and 0<=ny<m and graph[nx][ny]==graph[x][y]: 
                    cnt+=1
                else :
                    break
            if cnt == 3:
                result = max(result,d)
print((result+1)**2)

             


