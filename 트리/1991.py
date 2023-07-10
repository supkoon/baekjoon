'''
문제
트리순회 - DFS - 전위,중위,후위

아이디어
재귀. NLR, LNR, LRN

복잡도
O(logN)

변수
tree



'''

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right 


tree = {}

n = int(input())
for i in range(n):
    value,left,right = input().split() 
    tree[value] = Node(value,left,right)

def preorder(node):
    print(node.value,end='')
    if node.left !='.':
        preorder(tree[node.left])
    if node.right !='.':
        preorder(tree[node.right])

def inorder(node):
    if node.left !='.':
        inorder(tree[node.left])
    print(node.value,end='')
    if node.right !='.':
        inorder(tree[node.right])

def postorder(node):
    if node.left!='.':
        postorder(tree[node.left])
    if node.right!='.':
        postorder(tree[node.right])
    print(node.value,end='')

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])
