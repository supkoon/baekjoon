from collections import OrderedDict
num,p = map(int,(input().split()))
graph = OrderedDict()
while(True):
    result = sum(map(lambda x : x**p,map(int,list(str(num)))))
    if result in graph.keys():
        print(list(graph.keys()).index(result))
        break
    graph[num]=result
    num= result
# print(graph)