'''
문제
연산자 우선순위를 무시하고 앞에서부터 진행 
음수를 양수로 나눌떄 --> 양수로 바꾼뒤 몫을 취하고 음수로 바꾼것 
-(-n//k)

최대인 것과 최소인 것 구하기 .


bfs는 안되나? 될것같은데 ㅎㅎ visited 혹은 결과만들어서 계속 전파하기?

해서 안되면 dfs해보자 . 공부차원 ㅎㅎ 

'''



def solution(n,nums,cals):
    pass 

n=  int(input())
nums = list(map(int,input().split()))
cals = dict(zip(['+','-','*','//'],list(map(int,input().split()))))
print(n,nums,cals)
