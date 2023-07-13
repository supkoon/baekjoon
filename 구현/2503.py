'''
문제 
숫자 야구
1~9로 이루어진 세자리 수 
세자리 수를 말해서 셋중 하나가 자리까지 맞추면 스트라이크
다른 자리면 볼 

입력을 n번 하는데
n번을 하면서 출제자가 냈을 가능성 있는 수가 몇개인지 출력


아이디어

안되는애들을 전체 셋에서 제거함.
123 1 1 
2개 자리가 맞는애들 3개 자리가 맞는애들

1개 포함 
3개 포함 




result set 
each_set.add()
result_set.intersection(each_set)


복잡도


변수


'''

from itertools import combinations,permutations

candidates = []
candidates = list(range(1,10))
candidates = list(permutations(candidates,3))

n = int(input())

for i in range(n):
    ans, num_s, num_b = map(int,input().split())
    ans = list(map(int,list(str(ans))))

    for idx,candidate in enumerate(candidates):
        cnt=0 
        if candidate!=-1:
            for i in range(3):
                if candidate[i] == ans[i]:
                    cnt+=1
            if cnt != num_s:
                candidates[idx] = -1
                continue
        cnt=0
        if candidate!=-1:
            for i in range(3):    
                if ans[i] in candidate :
                    cnt+=1
            if cnt != (num_b+num_s):          
                candidates[idx] = -1 

print(sum([1 for candidate in candidates if candidate!=-1]))
