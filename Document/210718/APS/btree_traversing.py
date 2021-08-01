class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    # 삽입 메서드
    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

    # 탐색 메서드
    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)

    # 삭제 메서드
    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted

    def _delete_value(self, node, key):
        if node is None:
            return node, False

        deleted = False
        if key == node.data:
            deleted = True
            if node.left and node.right:
                # replace the node to the leftmost of node.right
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self._delete_value(node.left, key)
        else:
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted

    # 전위 순회
    def pre_order_traversal(self):
        def _pre_order_traversal(root):
            if root is None:
                pass
            else:
                print(root.data)
                _pre_order_traversal(root.left)
                _pre_order_traversal(root.right)
        _pre_order_traversal(self.root)
    
    # 정위 순회
    def in_order_traversal(self):
        def _in_order_traversal(root):
            if root is None:
                pass
            else:
                _in_order_traversal(root.left)
                print(root.data)
                _in_order_traversal(root.right)
        _in_order_traversal(self.root)
    
    # 후위 순회
    def post_order_traversal(self):
        def _post_order_traversal(root):
            if root is None:
                pass
            else:
                _post_order_traversal(root.left)
                _post_order_traversal(root.right)
                print(root.data)
        _post_order_traversal(self.root)

    # 너비 우선 순회
    def level_order_traversal(self):
        def _level_order_traversal(root):
            queue = [root]
            while queue:
                root = queue.pop(0)
                if root is not None:
                    print(root.data)
                    if root.left:
                        queue.append(root.left)
                    if root.right:
                        queue.append(root.right)
        _level_order_traversal(self.root)
    

    
array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]

bst = BinarySearchTree()
for x in array:
    bst.insert(x)

# Find
print(bst.find(15)) # True
print(bst.find(17)) # False

# # Delete
# print(bst.delete(55)) # True
# print(bst.delete(14)) # True
# print(bst.delete(11)) # False

# depth first
bst.pre_order_traversal()   # 40 4 34 14 13 15 45 55 48 47 49
bst.in_order_traversal()    # 4 13 14 15 34 40 45 47 48 49 55
bst.post_order_traversal()  # 13 15 14 34 4 47 49 48 55 45 40
# breadth first
bst.level_order_traversal() # 40 4 45 34 55 14 48 13 15 47 49

print(bst.delete(55)) # True

# depth first
bst.pre_order_traversal()   # 40 4 34 14 13 15 45 48 47 49
bst.in_order_traversal()    # 4 13 14 15 34 40 45 47 48 49
bst.post_order_traversal()  # 13 15 14 34 4 47 49 48 45 40
# breadth first
bst.level_order_traversal() # 40 4 45 34 48 14 47 49 13 15

print(bst.delete(14)) # True

# depth first
bst.pre_order_traversal()   # 40 4 34 15 13 45 48 47 49
bst.in_order_traversal()    # 4 13 15 34 40 45 47 48 49
bst.post_order_traversal()  # 13 15 34 4 47 49 48 45 40
# breadth first
bst.level_order_traversal() # 40 4 45 34 48 15 47 49 13

print(bst.delete(11)) # False

# depth first
bst.pre_order_traversal()   # 40 4 34 15 13 45 48 47 49
bst.in_order_traversal()    # 4 13 15 34 40 45 47 48 49
bst.post_order_traversal()  # 13 15 34 4 47 49 48 45 40
# breadth first
bst.level_order_traversal() # 40 4 45 34 48 15 47 49 13