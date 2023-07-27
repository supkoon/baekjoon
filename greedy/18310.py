'''
문제
마을에 집이 가로로 존재.
안테나를 설치

안테나로부터 모든 집까지의 거리 합이 최소가 되도록 설치

동일한 위치에 집이 여러개 있을 수 있음

아이디어
결국 거리의 합을 최소로 만드는 집 하나를 고르는 것. 
앞에서부터 해봄...> 안됨

O(N) or O(NlogN) 필요

그냥 중앙값이 답이라고함..

복잡도

'''


n = int(input())
locations = list(map(int,input().split()))
locations = sorted(locations)

print(locations[(n-1)//2])

