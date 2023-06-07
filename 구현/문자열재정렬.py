'''
아이디어
앞에서부터 그리디하게 진행.
ord('A')<x<ord('Z') 일때, list에 추가
아닐 시, result+=1

마지막에 정렬한번하면서 더하기 ?

시간복잡도
O(nlogn)?
100,000 * 5

변수
result1
result2

'''

string = input()

result1= []
result2=0
for x in string:
    if ord('A')<=ord(x)<=ord('Z'): # x.isalpha()!!!!!!!!
        result1.append(x)
    else:
        result2 += int(x)

if result2!=0:
    print(''.join(sorted(result1))+str(result2))
else:
    print(''.join(sorted(result1)))

    