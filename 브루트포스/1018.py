
a , b = map(int,input().split())

og = []
answer_w = 'WBWBWBWB'+'BWBWBWBW'+'WBWBWBWB'+'BWBWBWBW'+'WBWBWBWB'+'BWBWBWBW'+'WBWBWBWB'+'BWBWBWBW'

for i in range(a):
    og.append(input())
min_num = 64
for row in range(0,a-7):
    for col in range(0,b-7):
        count_w = 0
        count_b = 0
        result = ''
        case = og[row:row+8]

        for each_case in case : #각각 8x8 일렬로 .
            result+=each_case[col:col+8]

        for i in range(0,len(result)): #정답과 비교
            if answer_w[i] != result[i]:
                count_w+=1
            else : count_b +=1

        if min_num > min([count_w,count_b]): #최소라면 업데이트
            min_num = min([count_w,count_b])

print(min_num)