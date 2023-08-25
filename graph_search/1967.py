'''
문제
트리의 지름

두 노드를 양쪽으로 당겼을때, 가장 긴 거리.
가중치가 있는 간선.

아이디어
가중치가 있는 간선.
양의정수 거리, 모든 점에서 점까지 이기 떄문에, 플루이드 워셜.  

플로이드 워셜 --> 메모리 초과


'''
import sys 
from collections import deque
n = int(input())
graph = [[] for _ in range(n+1)]

for i in range(n-1):
    a,b,w = map(int,sys.stdin.readline().split())
    graph[a].append([b,w])
    graph[b].append([a,w])

def bfs(start):
    visited = [0 for _ in range(n+1)]
    queue=  deque()
    queue.append([start,0])
    visited[start]=1
    while(queue):
        expanded,cost = queue.popleft()
        for child,cost_child in graph[expanded]:
            if not visited[child]:
                visited[child]= visited[expanded] + cost_child
                queue.append([child,visited[child]])
    return visited.index(max(visited)),max(visited)-1

idx, _ = bfs(1)
_, result = bfs(idx)
print(result)



# INF = 101
# dist = [[INF]*(n+1) for _ in range(n+1)]

# for i in range(n-1):
#     a,b,w = map(int,sys.stdin.readline().split())
#     dist[a][b] = w
#     dist[b][a] = w

# for s in range(1,n+1):
#     for m in range(1,n+1):
#         for e in range(1,n+1):
#             if dist[s][e] > dist[s][m] + dist[m][e]:
#                 dist[s][e] = dist[s][m] + dist[m][e]

# result = 0
# for i in dist[1:]:
#     for j in i[1:]:
#         result = max(result,j)
# print(result)  
