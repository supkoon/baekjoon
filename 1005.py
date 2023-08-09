'''
문제
ACM craft

아이디어
위상정렬 + dp
degree가 0이 될떄까지 해당 노드까지 자식들의 max값을 저장하고
0이되면 해당 노드의 소요시간과 더해줌 . 

복잡도 
O(v+e)

'''

import sys
from collections import deque 
t = int(input())

def topology_sort(graph,in_degree,dp,weights):
    queue = deque()
    
    for node in range(1,n+1):
        if in_degree[node]==0:
            queue.append(node)
            dp[node] = weights[node-1]

    while(queue):
        expanded = queue.popleft()
        
        for child in graph[expanded]:
            in_degree[child]-=1
            dp[child] = max( dp[expanded], dp[child] ) 
            if in_degree[child]==0:
                dp[child] = dp[child] + weights[child-1]
                queue.append(child)

    return dp

for case in range(t):
    n,k = map(int,sys.stdin.readline().split())
    weights = list(map(int,sys.stdin.readline().split()))
    dp = [0 for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    in_degree = [0 for _ in range(n+1)]

    for edge in range(k):
        s,e = map(int,sys.stdin.readline().split())
        graph[s].append(e)
        in_degree[e]+=1
    
    target = int(input())
    dp = topology_sort(graph,in_degree,dp,weights)
    print(dp[target])





    

