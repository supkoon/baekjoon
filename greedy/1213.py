from collections import Counter
string = list(input())
word_count = Counter(string)
check = [word_count%2==1 for word_count in word_count.values()]
result = ""
if sum(check) in [0,1] :
    #홀수인게 0개 혹은 1개여야함. (1개인 경우는 mid)
    mid = ""
    for item,value in sorted(word_count.items(),key=  lambda x: x[0]):
        if value % 2 == 1:
            mid = item
        result += item * (value//2)
    result += mid + result[::-1]
    print(result)
else:
    print("I'm Sorry Hansoo")
