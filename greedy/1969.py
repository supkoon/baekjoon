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
