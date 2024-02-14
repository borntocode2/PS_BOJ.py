class TreeNode:
    def __init__(self, data):
        # 노드의 데이터와 부모 노드, 자식 노드를 초기화합니다.
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self, child_node):
        # 자식 노드를 추가하고 부모-자식 관계를 설정합니다.
        child_node.parent = self
        self.children.append(child_node)

class Tree:
    def __init__(self, root):
        # 트리의 루트 노드를 초기화합니다.
        self.root = root

    def get_root(self):
        # 트리의 루트 노드를 반환합니다.
        return self.root

# 트리 노드 생성
root_node = TreeNode("Root")
child1 = TreeNode("Child 1")
child2 = TreeNode("Child 2")
child3 = TreeNode("Child 3")

# 부모-자식 관계 설정
root_node.add_child(child1)
root_node.add_child(child2)
child2.add_child(child3)

# 트리 생성
my_tree = Tree(root_node)

# 노드 및 관계 확인
print("Root 노드의 자식:", [child.data for child in my_tree.get_root().children])
print("Child 2의 부모:", child2.parent.data)
print("Child 3의 부모:", child3.parent.data)