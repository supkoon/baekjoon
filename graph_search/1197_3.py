'''
MST

n-1개의 엣지로 n개 노드의 그래프를 잇는 방법.
가장 최소 간선합으로 만들어야함.

1. 엣지 가중치로 정렬
2. 해당 엣지를 포함시킬 것인가 말 것인가.
(루트 노드가 같은지로 판단)
3. 2를 반복 

'''
import sys 

v,e = map(int,sys.stdin.readline().split())
edges = [list(map(int,sys.stdin.readline().split())) for _ in range(e)]

edges.sort(key = lambda  X : X[2])
parent = [i for i in range(v+1)]

def find_root(parent,x):
    if parent[x] != x:
        parent[x] = find_root(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):

    a = find_root(parent,a)
    b = find_root(parent,b)

    if a < b:
        parent[b] = a 
    else:
        parent[a] = b 

result = 0 
for s,e,w in edges:
   
    if find_root(parent,s) != find_root(parent,e):
        union_parent(parent,s,e)
        result += w 

print(result)