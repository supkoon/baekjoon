'''
문제
연산자 우선순위를 무시하고 앞에서부터 진행 
음수를 양수로 나눌떄 --> 양수로 바꾼뒤 몫을 취하고 음수로 바꾼것 
-(-n//k)

최대인 것과 최소인 것 구하기 .


bfs는 안되나? 될것같은데 ㅎㅎ visited 혹은 결과만들어서 계속 전파하기?

해서 안되면 dfs해보자 . 공부차원 ㅎㅎ 

'''
from collections import deque

def bfs(n,start,cals):
    cnt=1
    queue = deque()
    queue.append([start,cnt,cals])
    max_result = -1e10
    min_result = 1e10
    while(queue):
        cur,cnt,cals_left = queue.popleft()
        if cnt == n:
            max_result = max(max_result,cur)
            min_result = min(min_result,cur)

        for cal,num in cals_left.items():
            if num:
                new_cals = cals_left.copy()
                if cal=='//' and cur<0:
                    new = -(-cur//nums[cnt]) 
                else: 
                    new = eval(str(cur)+cal+str(nums[cnt]))
                    
                new_cals[cal]-=1
                queue.append([new,cnt+1,new_cals])
                
    return max_result,min_result
    
def solution(n,nums,cals):
    max_result, min_result = bfs(n,nums[0],cals)
    return max_result,min_result 

n=  int(input())
nums = list(map(int,input().split()))
cals = dict(zip(['+','-','*','//'],list(map(int,input().split()))))
result = solution(n,nums,cals) 
print(result[0])
print(result[1])

