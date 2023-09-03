'''
문제
연산자 끼워넣기

아이디어
bfs는 되는것 확인
dfs + 백트랙킹으로 풀어보기 
불필요한 copy가 일어나지 않을 것으로 판단함. 




'''
min_result = 1e10
max_result = -1e10 #항상 계산결과는 min max 범위 확인. max가 음이 가능할떄는 0 주는것 주의. 그냥 항상 -1e10주는게 나을듯 
def dfs(cnt, cur, cals): #현재길이, 현재값, 연산자
    global min_result, max_result, n 
    if n==cnt:
        min_result = min(min_result,cur)
        max_result = max(max_result,cur)
        return 
    
    for oper,num in cals.items():
        if num:
            cals[oper]-=1
            if oper =='//' and cur<0:
                new = -(-cur//nums[cnt])
            else:
                new = eval(str(cur)+oper+str(nums[cnt]))
            dfs(cnt+1,new,cals)
            cals[oper]+=1
            
def solution(n,nums,cals):
    pass

n = int(input())
nums = list(map(int,input().split()))
cals  = dict(zip(['+','-','*','//'],list(map(int,input().split()))))
dfs(1,nums[0],cals)
print(max_result)
print(min_result)
