'''
아이디어 : 
그리디.

리스트에 담아서 마지막부터 순회.

마지막부터 몫+=, 나머지를 유지

복잡도: O(N)

변수 : 
nums = []
cnt = 0
'''

n,k = map(int,input().split())

nums = []
cnt=0
for i in range(n):
    nums.append(int(input()))


for i in nums[::-1]:
    cnt += k//i
    k = k % i
    
print(cnt)
    

