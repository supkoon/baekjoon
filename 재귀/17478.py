def recursive(n):
        global count
        if count == n: return
        while(count<n):
                count+=1
                print('____'*(n-1)+'"재귀함수가 뭔가요?"')
                print('____' * (n - 1) + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
                print('____' * (n - 1) + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
                print('____' * (n - 1) + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
                recursive(n+1)
                print('____' * (n - 1) + "라고 답변하였지.")

n = int(input())
recursive(n)
