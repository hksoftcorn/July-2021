# 업무일지

### ✔ Summary

- [x] 08:00~10:00 봉선사 연꽃축제
- [x] 11:00~13:00 송추 평양면옥
- [x] 14:00~16:30 휴식 & 카페
- [x] 16:30~18:00 APS
- [x] 21:00~24:00 APS2, 면접준비



## ✨ 오늘 배운 내용

- [객체지향 프로그래밍](./APS/객체지향2.md)




## 👀 수행한 업무 및 작성한 코드

- 

```python
# Linked List
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
     
    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            whlie node.next:
                node = node.next
            node.next = Node(data)
        
    def desc(self):
        node = self.head
        while node:
            node = node.next
        
def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)

    
```

```python
# N-queen

n = int(input())

def is_available(candidate, current_col):
    current_row = len(candidate)
    for queen_row in range(current_row):
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            return False
    return True


def DFS(N, current_row, current_candidate, final_result):
    if current_row == N:
        final_result.append(current_candidate[:])
        return
    for candidate_col in range(N): # 0, 1, 2, 3
        if is_available(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            DFS(N, current_row + 1, current_candidate, final_result)
            current_candidate.pop()


def solve_n_queens(N):
    final_result = []
    DFS(N, 0, [], final_result)
    return final_result


print(solve_n_queens(n))
```

```python
# N-queen shorter version

def is_promising(v):
    for i in range(v):
        if row[v] == row[i]:
            return False
        if abs(row[v] - row[i]) == v - i:
            return False
    return True

def dfs(v):
    global cnt
    if v == N:
        cnt += 1
        result.append(row[:])
    else:
        for i in range(N):
            row[v] = i
            if is_promising(v):
                dfs(v + 1)

N = int(input())
cnt = 0
row = [0] * N
result = []
dfs(0)
print(result)
```



## 🐱‍💻 아쉬운 점 & 느낀 점

- boj n-queen 문제가 안 풀린다...

 

