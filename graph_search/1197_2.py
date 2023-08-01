'''
최소 스패닝 트리 복습


아이디어
간선을 정렬 --> 해당 간선을 스패닝 트리에 포함시킬지 판단(판단 기준은 루트 노드가 다른가)
--> 반복 


'''
import sys 
v,e = map(int,sys.stdin.readline().split())
edges = [list(map(int,sys.stdin.readline().split())) for _ in range(e)]
parent = [i for i in range(v+1)]

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    
    s = find_parent(parent,a)
    e = find_parent(parent,b)

    if s < e:
        parent[e] = s 
    else :
        parent[s] = e 


edges.sort(key = lambda x : x[2])

result = 0 
for s,e,w in edges:
    if find_parent(parent,s) != find_parent(parent,e):
        union_parent(parent,s,e)
        result += w 
print(result)

