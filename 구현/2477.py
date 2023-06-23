'''
아이디어

1. 현재의 위치를 기준으로 하나씩 받으면서 
4,3 중에 큰값 저장 
1,2 중에 큰값 저장
--> 큰 넓이

2. 작은 넓이 구하기
리스트를 두배로 복사한다음,
4콤보 이어지는 구간에 중간값을 곱해서 구함.

최대 x 최대 - 작은 네모

복잡도
O(n)


변수
graph = [[]]
cnt,cnt_2 : 두번나온애들 기록
h_max 
w_max
combo : 몇번연속인지.

'''

n = int(input())
graph = []
cnt = [0]*5
h_max = 0
w_max = 0 
for i in range(6):
    direction,length = map(int,input().split())
    if direction in [3,4]:
        h_max = max(h_max,length)
    else:
        w_max = max(w_max,length)
    cnt[direction]+=1
    graph.append([direction,length])

graph = graph*2 
cnt_2 = [i for i in range(len(cnt)) if cnt[i]==2]

combo =  0
idxs = []
for i in range(len(graph)):
    direction,length = graph[i]
    if direction in cnt_2:
        combo+=1
        idxs.append(i)
        if combo==4:
            small = graph[idxs[1]][1]*graph[idxs[2]][1]
    else:
        combo=0
        idxs=[]
    
print(n*(h_max*w_max-small))
