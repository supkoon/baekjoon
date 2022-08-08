a = input()
b = input()
dp = []
for i in range(len(a)):
    dp.append(int(a[i]))
    dp.append(int(b[i]))

for i in range(16,2,-1):
    temp = []
    for j in range(i-1):
        temp.append((dp[j]+dp[j+1])%10)
    dp = temp
print(str(dp[0])+str(dp[1]))

