# Heapq를 활용한 다익스트라

- Heapq를 활용하는 방법에 대하여 알아보았습니다.
- 중요한 점!!  `float('inf')`를 이용하자...
  - 12진수의 최대 수 : 0xfffffff 로 큰 수를 표현했는데,, 무한의 수를 잡아내지 못하는 것 같습니다... inf로 초기화 해줍시다!

```python
# 1753 최단경로

# dijkstra 문제풀이 heap 사용해보기
import heapq

V, E = map(int, input().split())
K = int(input())
G = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
dist = [0xfffffff] * (V + 1)

def dijkstra(start):
    Q = []
    heapq.heappush(Q, (0, start))
    dist[start] = 0

    while Q:
        d, u = heapq.heappop(Q)
        if dist[u] < d: continue

        for ele in G[u]:
            v, w = ele
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(Q, (dist[v], v))

dijkstra(K)
for i in range(1, V + 1):
    if i == K:
        print(0)
    elif dist[i] == 0xfffffff:
        print('INF')
    else:
        print(dist[i])             
```

```python
# 17396 백도어

import heapq

V, E = map(int, input().split())
enemy = list(map(int, input().split())) # 1은 x
enemy[-1] = 0
G = [[] for _ in range(V)]
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))

dist = [float('inf')] * V

def dijkstra(start):
    Q = []
    heapq.heappush(Q, (0, start))
    dist[start] = 0

    while Q:
        d, u = heapq.heappop(Q)
        if dist[u] < d: continue

        for v, w in G[u]:
            if enemy[v]: continue
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(Q, (dist[v], v))

dijkstra(0)

if dist[V - 1] == float('inf'):
    print(-1)
else:
    print(dist[V - 1])

```

