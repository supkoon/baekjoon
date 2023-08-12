'''
문제 
DNA에서
Hamming Distance란 문자가 다른 것의 개수
DNA가 주어졌을때, 
distance 합이 가장 작은 dna를 구하기. 


아이디어


복잡도

'''

import sys 
n,m = map(int,input().split())

dnas = []
for i in range(n):
    dnas.append(sys.stdin.readline().rstrip())


result =''
result_cnt = 0
for i in range(m):
    cnt_t, cnt_a, cnt_g, cnt_c = 0,0,0,0
    min_idx = 'T'
    min_cnt = 1e10
    for dna in dnas:
        if dna[i]=='T':
            cnt_a += 1
            cnt_g += 1
            cnt_c += 1

        elif dna[i] =='A':
            cnt_c += 1
            cnt_t += 1
            cnt_g += 1

        elif dna[i] == 'G':
            cnt_a += 1
            cnt_t += 1
            cnt_c += 1

        else:
            cnt_t += 1
            cnt_a += 1
            cnt_g += 1
        
    for dna,cnt in zip(['T','G','C','A'],[cnt_t,cnt_g,cnt_c,cnt_a]):
        if min_cnt >= cnt:
            min_idx = dna
            min_cnt = cnt

    result += min_idx
    result_cnt += min_cnt  

print(result)
print(result_cnt)
               
