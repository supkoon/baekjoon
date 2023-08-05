'''
문제
n명의 사람
m명의 비교
를 가지고 가능한 줄 세우기


아이디어
위상정렬

위상정렬하는법
indegree를 정의하고,
indegree가 0인 노드를 순서대로 방문하면서,
out edge를 자름. 해당 도착 노드의 indegree가 따라서 낮아짐.
0이 되면 queue에 넣음.


'''
import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]

result = []

for edge in range(m):
    s,e = map(int,sys.stdin.readline().split())
    graph[s].append(e)
    indegree[e] +=1


def topology_sort():
    queue = deque()
    
    for node in range(1,n+1):
        if indegree[node]==0:
            queue.append(node)
    
    while(queue):
        expanded = queue.popleft()
        result.append(expanded)
        for child in graph[expanded]:
            indegree[child]-=1
            if indegree[child]==0:
                queue.append(child)
                
topology_sort()

print(*result)
        