def self_num(a):
    result = a
    a = str(a)
    for i in range(len(a)):
        result += int(a[i])
    return result

result = [ ]
for i in range(1,10001):
    num = self_num(i)
    if num not in result:
        result.append(num)

result = sorted(list(set(list(range(1,10001)))-set(result)))

for i in result:
    print(i)
