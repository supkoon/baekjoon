import sys
import heapq

#힙 : 우선순위 큐를 위해 만들어짐.
#큐에 우선순위 개념을 도입
#우선순위 큐 : 우선순위가 높은것이 먼저 return

#우선순위 큐는 배열,연결리스트,힙으로 구현가능.
#힙이 가장 효율적
#삽입, 삭제 -- O(logn)
#완전 이진트리의 일종
#최대 힙:부모 노드의 키 값이 자식 노드의 키 값보다 항상 크거나 같음
#최소 힙:부모 노드의 키 값이 자식 노드의 키 값보다 항상 작거나 같음
n = int(input())
heap = []

#최대 힙
for _ in range(n):
    n = int(sys.stdin.readline())
    if n:
        heapq.heappush(heap,n)
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)