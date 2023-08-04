'''
문제

컴퓨터와 컴퓨터를 연결해야함
모든 컴퓨터를 연결해야함 

컴퓨터를 연결하는 비용을 최소로 하고싶음. 

아이디어
최소스패닝트리? 

복잡도
간선 정렬에 따라 다름.
보통의 정렬 알고리즘은 NlogN 구현
--> O(N logN) 

'''

import sys 
n = int(input())
m = int(input())
edges = []

INF = 1e10

parent = [i for i in range(n+1)]

for i in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    edges.append([a,b,c])

edges.sort(key = lambda x: x[2])

def find_root(x):
    if x!=parent[x]:
        parent[x] = find_root(parent[x])
    return parent[x]

def union_parent(a,b):
    a = find_root(a)
    b = find_root(b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b 

ans =0 
for s,e,w in edges:
    if find_root(s)==find_root(e):
        continue
    else:
        union_parent(s,e)
        ans+=w
print(ans)