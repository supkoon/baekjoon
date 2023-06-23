'''
아이디어
바꿀 위치도 주지 않음.
따라서 브루트포스 느낌이 나긴 함. 

그럼 어떻게 할거냐...

일단 중첩 for로 각각 돌려야할듯. 근데 여기서 얼마나 효율을 더 가지갈거냐.


1. 중첩 for로 모든 위치에서 각각 4가지 경우 고려
2. 가로, 세로콤보를 각각의 경우에서 계산 


추가 : 바꿔도 같다면 계산 안하는것


복잡도
O(n^4)

변수 
n, graph, combo(), result, 

'''

n = int(input())

graph = []
for i in range(n):
    line = list(input())
    graph.append(line)

result = 0
def combo():
    global n, graph
    #가로
    row_combo, col_combo, row_max, col_max =1,1,0,0
    for i in range(n):
        for j in range(n-1):
            if graph[i][j]==graph[i][j+1]:
                row_combo += 1
            else:
                row_combo = 1
            if row_max < row_combo:
                row_max = row_combo
        row_combo = 1

    for i in range(n):
        for j in range(n-1):
            if graph[j][i]==graph[j+1][i]:
                col_combo += 1
            else:
                col_combo = 1
            if col_max < col_combo:
                col_max = col_combo
        col_combo = 1 
    
    return max(col_max,row_max)
    #세로


for x in range(n):
    for y in range(n):
        for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]:
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny]!=graph[x][y]:
                    tmp = graph[nx][ny]
                    graph[nx][ny] = graph[x][y]
                    graph[x][y] = tmp
                    result = max(result,combo())
                    graph[x][y] = graph[nx][ny]
                    graph[nx][ny] = tmp 

print(result)