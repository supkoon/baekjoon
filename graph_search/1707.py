'''
문제
이분그래프(bipartite)인지 판별

아이디어
시작점으로부터 홀짝홀짝 넣어줌.
만약 홀짝홀짝이 저장되어 있을때, 같은 홀or짝이면 return false 



복잡도

'''
import sys
from collections import deque 
k = int(input())

def bfs(node):
    global graph,visited
    queue = deque()
    queue.append(node)
    visited[node]=1
    
    while(queue):
        expanded = queue.popleft()
        for child in graph[expanded]:
            if not visited[child]:
                visited[child]=visited[expanded]+1
                queue.append(child)
    

for case in range(k):
    v,e = map(int,sys.stdin.readline().split())
    edges = []
    visited = [0 for _ in range(v+1)]
    graph = [[] for _ in range(v+1)]
    for edge in range(e):
        s,e = map(int,sys.stdin.readline().split())
        edges.append([s,e])
        graph[s].append(e)
        graph[e].append(s)

    
    for node in range(1,v+1):
        if not visited[node]:
            bfs(node)
    
    
    visited = list(map(lambda x :x%2,visited))
    result = 'YES'
    for edge in edges:
        if visited[edge[0]] == visited[edge[1]]:
            result = 'NO'
            break
    print(result)
    