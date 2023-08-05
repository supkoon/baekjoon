'''
문제
줄세우기

답이 여러개면 아무거나 출력 


아이디어
N명의 학생 ( ~ 32000)
M명의 줄 (100000)

일단 n,m이 큰 것을 보니 O(logn)이하의 알고리즘 필요해보임 

위상정렬로 풀어야함
위상정렬 --> 방향성이 주어질때, 주어진 순서에 거르지 않고  나열하는것
directed graph에 적용가능.
indegree가 0인 노드들을 큐에서 꺼내 지속적으로 out edge를 지워줌. 


dfs를 활용하여 구현 가능

복잡도
O(V+E)

'''


import sys 
from collections import deque
n,m = map(int,sys.stdin.readline().split())
indegree = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]


for _ in range(m):
    s,e = map(int,sys.stdin.readline().split())
    graph[s].append(e)
    indegree[e]+=1
#directed
    result = []

def topology_sort():
    queue = deque()

    for node in range(1,n+1):
        if indegree[node]==0:
            queue.append(node)
    #indegree가 0인 노드 삽입 

    while(queue):
        expanded = queue.popleft()
        result.append(expanded)

        for child in graph[expanded]:
            indegree[child]-=1
            if indegree[child]==0:
                queue.append(child)

topology_sort()

print(*result)