'''
문제 
전위,중위,후위 순회 출력.

아이디어
이진트리 순회문제. 

복잡도
log(n)

변수

'''
class Node():
    def __init__(self,item,left,right):
        self.item = item
        self.left = left
        self.right = right 


def preorder(node):
    print(node.item, end='')
    if node.left != '.':
        preorder(tree[node.left])
    if node.right !='.':
        preorder(tree[node.right])

def inorder(node):
    if node.left !='.':
        inorder(tree[node.left])
    print(node.item, end='')
    if node.right !='.':
        inorder(tree[node.right])

def postorder(node):
    if node.left !='.':
        postorder(tree[node.left])
    if node.right !='.':
        postorder(tree[node.right])
    print(node.item,end='')



n = int(input())
inputs = []
tree = {}
for _ in range(n):
    item,left,right = input().split()
    tree[item] = Node(item,left,right)
preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])