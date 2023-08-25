'''
문제
단어수학
N개의 단어
각 단어는 대문자
대문자를 0부터 9까지로 바꿈(같은 알파벳은 같은 문자)
N개의 수를 합

아이디어
'''
import sys 
n = int(input())
words = {}
for i in range(n):
    word = list(sys.stdin.readline().rstrip())
    n = 10**(len(word)-1)
    for char in word:
        if char not in words:
            words[char] = 0
        words[char] += n
        n//=10

words = sorted(words.items(),key=lambda x:x[1],reverse=True)
result = 0 
for idx,i in enumerate(range(9,9-len(words),-1)):
    result += words[idx][1]*i
print(result)    