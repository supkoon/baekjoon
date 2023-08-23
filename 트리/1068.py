'''
문제
트리노드 자르기

아이디어
dfs를 사용해서 자르기.
그래프 정의하고 bfs도 가능
'''

n = int(input())
graph = [[] for _ in range(n)]
arr = list(map(int,input().split()))

for child,parent in enumerate(arr):
    if parent == -1:
        continue
    graph[parent].append(child)

k = int(input())

def dfs(node):
    arr[node]=-2
    for child in graph[node]:
        dfs(child)    

dfs(k)
result = 0
for i in range(len(arr)):
    if arr[i] !=-2 and i not in arr:
        result+=1
print(result)
        



