'''
문제
상근이 여행
도로가 깊이 k의 완전 이진트리
들어간 빌딩 순서를 리스트로 가지고 있음.
left - node - right 순서로 중위 방문했음.

방문 순서를 가지고 트리 복원

아이디어
노드 i의 left 2i, right 2i+1
중위순회하여 복원

복잡도
O(logn)

변수
k, order
tree
'''

k  = int(input())
order = list(map(int,input().split()))
tree = [0]*(2**k) #첫번쨰노드 x
idx=0
def inorder(node):
    global idx
    if node<2**k:
        inorder(2*node)
        tree[node] = order[idx]
        idx+=1
        inorder(2*node+1)
inorder(1)

n=1
while(n < 2**k):
    for i in range(n,2*n):
        print(tree[i],end=' ')
    n*=2
    print()
