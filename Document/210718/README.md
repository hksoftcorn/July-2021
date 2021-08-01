# 업무일지

### ✔ Summary

- [x] 08:00~12:00 [강의] 피그마 실습
- [x] 14:00~17:00 [APS] 문제풀이, 자료구조
- [x] 17:30~21:00 [Dinner] 스웨덴 수범이형 저녁식사
- [x] 22:00~02:00 [면접대비] 기사 3개 분석, 면접 스크립트
- [ ] ~~24:00~01:00 [프로젝트] Ref 찾기~~



## ✨ 오늘 배운 내용

- [우선순위큐 & 다익스트라](./APS/우선순위큐_다익스트라.md)



## 👀 수행한 업무 및 작성한 코드

- 김은지님 (중앙대 조교수) 코드로 B-Tree를 살펴보았다. [link](http://ejklike.github.io/2018/01/09/traversing-a-binary-tree-1.html)
  - 이러한 블로그 글에서 정제된 코드를 만날 수 있어서 놀라웠다.
  - 또한 대학 전공에서 위와같은 교수님, 숙련자들의 코드를 보면서 공부했겠구나 하고 내심 부러웠다.
  - 좋은 멘토가 될 수 있는 코드를 만나서 아주 만족스러운 하루가 되었다. 
  - => 나 또한 향기나는 코드를 작성하고 싶다.

```python
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
    
array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]

bst = BinarySearchTree()
for x in array:
    bst.insert(x)

# Find
print(bst.find(15)) # True
print(bst.find(17)) # False

# Delete
print(bst.delete(55)) # True
print(bst.delete(14)) # True
print(bst.delete(11)) # False
```







## 🐱‍💻 아쉬운 점 & 느낀 점

- 자료구조에 대한 튼튼한 기초가 필요하다

- 알고리즘이라는게 결국 기반은 자료구조!

- 클래스로 OOP 연습하기

- 클린 코드 고민하기

  

