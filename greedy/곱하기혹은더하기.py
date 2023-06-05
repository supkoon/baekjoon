'''
1 이하일 시 더하기 수행.
나머지 곱하기 수행.
1, n까지 반복

더하기가 더 좋은경우 : 각 숫자가 1 이하일때, 현재 숫자가 1 이하일때


복잡도 : 선형

변수 : result

'''


num = list(map(int,list(input())))

print(num)
result = 0
for digit in num:
        if digit <=1 or result <=1:
            result+=digit
        else:
            result*=digit

print(result)



