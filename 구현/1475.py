'''
문제
방번호
0번에서 9번까지 번호 한세트 
번호가 있을때, 몇 세트 필요한지(6,9 서로 뒤집어사용가능)


'''

n = input()

result = [0]*10
for i in n:
    result[int(i)]+=1
result[9] += result[6]
result[6]=0
if result[9]%2==1:
    result[9] = result[9]//2+1
else:
    result[9] = result[9]//2

print(max(result))

