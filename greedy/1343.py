'''
문제
폴리오미노 

AAAA와 BB를 무한대로 가지고있음
.과 X로 이루어진 보드판을
폴리오미노로 덮음
.는 덮으면안됨

아이디어
아... 하드코딩 했는데
그냥 replace하면 되네...

'''
board = input()

cnt =0 
result = ''
for i in range(len(board)):
    if board[i]=='X':
        cnt+=1
        if i== len(board)-1:
            if cnt%2==1:
                result = -1
                break
            if cnt//4:
                result += 'AAAA'*(cnt//4)
                cnt = cnt%4
            if cnt//2:
                result += 'BB'*(cnt//2)

    else:
        if cnt%2==1:
            result = -1
            break
        if cnt//4:
                result += 'AAAA'*(cnt//4) 
                cnt = cnt%4
        if cnt//2:
                result += 'BB'*(cnt//2) 
        result+='.'
        cnt=0

if result==-1:
    print(-1)

else:
    print(''.join(result))




