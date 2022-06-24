import sys
import copy

n,m = map(int,sys.stdin.readline().split())
graph=  [[] for node in range(n+1)]

for i in range(m):
    start,end = map(int,sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

day = 0
cnt=[]

while(True):
    cnt_day =0
    graph_next = copy.deepcopy(graph)
    for idx,node in enumerate(graph):
        for child in graph[idx]:
            for child_child in graph[child]:
                if child_child not in graph_next[idx] and child_child!=idx:
                    cnt_day+=1
                    graph_next[idx].append(child_child)
                    graph_next[child_child].append(idx)
    if cnt_day ==0:
        break
    else :
        cnt.append(cnt_day)
        day += 1
    graph = graph_next

print(day)
for i in cnt:
    print(i)