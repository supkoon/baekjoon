string = list(input())
alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
num = list('22233344455566677778889999')

alpha_to_num = {}
for i in range(26):
    alpha_to_num.update({alpha[i]:int(num[i])+1})
#zip 가능
result =  0
for i in string:
    result += alpha_to_num[i]

print(result)

