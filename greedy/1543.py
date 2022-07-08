string = input()
word = input()
len_word = len(word)
index=0
cnt=0
while(True):
    if index>=len(string):
        break
    if string[index:index+len_word]==word:
        index+=len_word
        cnt+=1
    else:
        index+=1
print(cnt)


