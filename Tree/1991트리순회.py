# input ex)
# A B C    A가 항상 루트노드 B는 왼쪽 자식노드, C는 오른쪽 자식노드
# B D .
# C E F
# E . .
# F . G
# D . .
# G . .
# 전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
# 중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
# 후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
N = int(input())
tree = {}
answer = []
for i in range(N):
    root, left, rigth = map(str, input().split())
    tree[root] = [left, rigth]

def preorder(root):
    if root != ".":
        answer.append(root)
        preorder(tree[root][0])
        preorder(tree[root][1])

def inorder(root):
    if root != ".":
        inorder(tree[root][0])
        answer.append(root)
        inorder(tree[root][1])
    
def postorder(root):
    if root != ".":
        postorder(tree[root][0])
        postorder(tree[root][1])
        answer.append(root)

preorder("A")
print(*answer, sep = "")
answer.clear()

inorder("A")
print(*answer, sep = "")
answer.clear()

postorder("A")
print(*answer, sep = "")
    