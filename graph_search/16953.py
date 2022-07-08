import sys
a,b = map(int,sys.stdin.readline().split())
depth = 0
graph = [[],[a]]
if a==b:
    sys.stdout.write(str(1))
else:
    answer = False
    #expand until find goal
    while(not answer):
        depth+=1
        depth_result = []
        for node in graph[depth]:
            left = node*2
            right = node*10+1
            if left<=b:
                depth_result.append(left)
            if right<=b:
                depth_result.append(right)
            #found goal
            if b in [left,right]:
                sys.stdout.write(str(depth+1))
                answer = True
                break
        #all nodes over goal = empty
        if not depth_result:
            sys.stdout.write(str(-1))
            break
        graph.append(depth_result)

