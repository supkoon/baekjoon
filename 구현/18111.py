'''
아이디어

집을 짓기위해 땅고르기 
집터 n,m
집터의 땅의 높이를 일정하게 바꾸는것

작업
1. i,j의 블록을 제거하여 인벤토리에 넣기 - 2초
2. 인벤토리에서 블럭을 꺼내 블록 쌓기 - 1초

0부터 가장 높은 높이까지 모두 진행해보기 -brute force
블록을 모두 회수해서, h*m*n <= num_block 인지 확인 
확인 후, 최저 time이면 저장

복잡도

O(n^3)

변수
n,m,b : x,y,가진 블록수
b_total : 총 블럭수
curr_time : 현재 계산하는 경우의 시간
gap : 각 블럭위치에서 블럭 수 차이

highest : 최대 높이
result_time : 만족하는 최저시간
result_h : 만족하는 최대높이

'''

n,m,b = map(int,input().split())
graph = []

for i in range(n):
    line = list(map(int,input().split()))
    graph.append(line)
    for j in range(m):
        if line[j]>highest:
            highest=line[j]

def fit():
    global n,m,b,graph
    result_h = 0
    result_time = 1e10
    b_total = 0
    for i in range(n):
        for j in range(m):
            b_total+= graph[i][j]
        
    for h in range(highest+1):
        if b_total>=h*m*n :
            curr_time = 0 
            for i in range(n):
                for j in range(m):
                    gap = h - graph[i][j]
                    if gap>=0:
                        curr_time += gap
                    else:
                        curr_time += gap*-2

            if result_time >= curr_time:
                result_h = h
                result_time=curr_time
    print(result_time,result_h)
fit()
