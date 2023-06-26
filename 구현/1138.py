'''
내용 

한줄로 서기.
아침마다 오민식 맘대로 한줄로 서는 마을. 
사람들으 ㄴ자기보다 큰 사람이 왼쪽에 몇명 있는지만 기억.
사람 n명의 키는 순서대로 1~n. 모두 다름. 

아이디어
1의 자리는 바로 정해짐. 
2의 자리는 1의 자리가 정해지면 바로 정해짐.
3의 자리는 2의 자리가 정해지면 바로 정해짐.

큰것만 재면 되기 때문에, 각 자리에서 앞에 남은 공간을 새면됨. 
...

복잡도
O(n^3)

변수
n 사람수
num 각 왼쪽 몇명인지. 
result = []
'''

# n = int(input())
# # num = [0]+list(map(int,input().split()))
# result = [0]*(n+1)
# for i in range(1,n+1):  #1부터 n까지
#     flag = 0
#     for j in range(1,n+1): #각 자리를 시도함. 
#         cnt=0
#         for k in range(1,j+1): #하나 이전까지 왼쪽에 빈자리 몇개 남았는지. 
#             if k==j:
#                 if cnt == num[i] and result[j]==0:
#                     result[j]=i    
#                     flag = 1
#             if result[k] == 0: 
#                 cnt+=1
#         if flag : break
            
            
# print(' '.join(list(map(str,result[1:]))))
                
n = int(input())
nums = list(map(int,input().split()))
result = [0]*n
for i in range(n):
    cnt = 0 
    for j in range(n):
        if nums[i] == cnt and result[j]==0:
            result[j] = i+1
            break
        if result[j]==0:
            cnt+=1

print(*result)


        
