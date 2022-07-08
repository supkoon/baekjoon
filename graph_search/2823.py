import sys
r,c = map(int,sys.stdin.readline().split())

road_map = [list(sys.stdin.readline().rstrip()) for line in range(r)]
graph = [[0 for i in range(c)] for node in range(r)]

direction_x = [-1,0,0,1]
direction_y = [0,1,-1,0]

for i in range(r):
    for j in range(c):
        if road_map[i][j]=='.':
            for direction in range(4):
                i_neighbor=i+direction_x[direction]
                j_neighbor=j+direction_y[direction]
                if 0<=i_neighbor<r and 0<=j_neighbor<c:
                    neighbor = road_map[i_neighbor][j_neighbor]
                    if neighbor=='.':
                        graph[i][j]+=1
result = 0
for i in range(r):
    for j in range(c):
        if graph[i][j]==1:
            result=1

print(result)


