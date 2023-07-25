'''
문제
상근이가 가봤던 곳 찾기
루트에서 시작 중위순회?
왼쪽자식 - node - 오른쪽자식

아이디어
트리는 2^k-1개로 이루어짐. 

노드를 리스트에 저장하는 경우,
i번째 인덱스에 있는 노드의 왼쪽 자식은 i×2,
오른쪽 자식은 i×2+1입니다.


복잡도


변수
k 깊이
order 방문순서 
'''


k = int(input())
order = list(map(int,input().split()))

n = 2**k
tree = [0]*n
idx =0 

def inorder(node):
    global idx
    
    #중위순회
    if node < n :
        inorder(node * 2)
        tree[node] = order[idx]
        print(idx, node)
        idx +=1
        inorder(node * 2 + 1)

inorder(1)  #idx 1의 노드부터 (노드 건물번호 아님)
idx = 1 

while(idx<n):
    for i in range(idx,idx*2):
        print(tree[i], end = ' ')
    print()
    idx *=2
