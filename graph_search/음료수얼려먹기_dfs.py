def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    
    if graph[x][y] == 0:
        graph[x][y]=1

        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False 

import time
t1 = time.time()
n,m = map(int,input().split())
graph = []

for i in range(n):
    line = list(map(int,input()))
    graph.append(line)    

result = 0

for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result+=1
t2 = time.time()
print(t2-t1)
print(result)
        

