'''
아이디어 : 단순한 dfs bfs 탐색


복잡도 :
O(n^2)

변수 : 
graph
visited * 2 
'''
from collections import deque

def bfs(s):
    queue = deque()
    queue.append(s)
    visited_bfs[s]=1
    while(queue):
        expanded = queue.popleft()
        print(expanded,end=' ')
        for child in graph[expanded]:
            if not visited_bfs[child]:
                queue.append(child)
                visited_bfs[child]=1
                


def dfs(s):
    visited_dfs[s]=True
    print(s,end = ' ')
    for child in graph[s]:
        if not visited_dfs[child]:
            dfs(child)

        


n,m,s = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited_bfs = [0]*(n+1)
visited_dfs = [0]*(n+1)

for i in range(m):
    start,end = map(int,input().split()) 
    graph[start].append(end)
    graph[end].append(start)

graph = list(map(sorted,graph))

dfs(s)
print()
bfs(s)




