'''
문제
요세푸스 문제
1~n n명 있고 k번쨰가 나감. 그다음엔 사라진 사람 이전사람 기준 k 번째가 또 나감. 반복.

아이디어
큐 사용.
앞에서 k-1개 popleft 후 popleft
pop한거 다시 push


복잡도

변수

'''
from collections import deque

n, k = map(int,input().split())

queue = deque()

for i in range(1,n+1):
    queue.append(i)

result = []
while(queue):
    tmp = []
    loop_range =  (k-1)%len(queue)
    
    for i in range(loop_range):
        tmp.append(queue.popleft())
    result.append(str(queue.popleft()))
    for i in range(loop_range):
        queue.append(tmp[i])
print('<'+', '.join(result)+'>')

    