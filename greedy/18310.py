'''
문제
마을에 집이 가로로 존재.
안테나를 설치

안테나로부터 모든 집까지의 거리 합이 최소가 되도록 설치

동일한 위치에 집이 여러개 있을 수 있음

아이디어
결국 거리의 합을 최소로 만드는 집 하나를 고르는 것. 



복잡도

'''


n = int(input())
locations = list(map(int,input().split()))
locations = sorted(locations)
best = 1e10
best_loc = 0
for loc in locations:
    result = sum(list(map(lambda x : abs(x-loc), locations)))
    if result < best :
        best=result
        best_loc = loc
print(best_loc)
