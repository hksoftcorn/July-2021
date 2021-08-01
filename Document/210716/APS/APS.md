# APS

- [x] 1060_최소비용신장트리
- [ ] 1863_종교
- [ ] 2467_비용
- [ ] 2997_트리(중)
- [ ] 3000_트리(고)



## 1. 상호배타 집합

> - 구현이 간단하고 동작 속도가 빠르기 때문에 그래프 영역에서 많이 사용되고 다른 알고리즘의 일부로 활용
> - 각 집합에 속한 원소의 수 관리

### 1.1. make_set(x)

```
def make_Set(x):
	p[x] = x
```



### 1.2. find_set(x)

```python
def find_set(x):
    if x == p[x]: return x
    else: return find_set(p[x])
```



### 1.3. union(x, y)

```python
def union(x, y):
    p[find_set(y)] = find_set(x)
```



### 1.4. 연산의 효율을 높이는 방법

#### 1.4.1. Rank를 이용한 Union

> - 각 노드는 자신을 루트로 하는 Subtree의 높이를 랭크라는 이름으로 저장
> - 두 집합을 합칠 때 Rank가 낮은 집합을 Rank가 높은 집합에 붙임



#### 1.4.2. Path compression

> - Find_set을 행하는 과정에서 만나는 모든 노드들이 직접 Root를 가리키도록 부모 정보를 변경



