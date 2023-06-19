'''
아이디어

집을 짓기위해 땅고르기 
집터 n,m
집터의 땅의 높이를 일정하게 바꾸는것

작업
1. i,j의 블록을 제거하여 인벤토리에 넣기 - 2초
2. 인벤토리에서 블럭을 꺼내 블록 쌓기 - 1초


최저, 최대 찾기. 


복잡도

변수
n,m,b : x,y,가진 블록수

'''

n,m,b = map(int,input().split())
graph = []

for i in range(n):
    line = list(map(int,input().split()))
    graph.append(line)

def fit():
    global m,n,b
    
    smallest = 1e10
    for i in range(n):
        for j in range(m):
            result = 0
            curr = b
            h = graph[i][j] 
            for k in range(n):
                for l in range(m):
                    gap = h-graph[k][l]
                    if gap >= 0:
                        result += gap
                        curr-=gap
                    elif gap < 0:
                        result += gap*-2
                        curr+=gap 
                
            if curr>=0:
                if result == smallest  :
                    if h > smallest_h:
                        smallest_h = h
                elif result < smallest :
                    smallest_h = h
                    smallest=result
  
    print(smallest,smallest_h)
    
fit()
