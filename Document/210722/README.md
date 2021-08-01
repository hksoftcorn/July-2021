# 업무일지

### ✔ Summary

- [x] 08:00~11:00 면접준비
- [x] 12:00~15:00 국민은행 면접
- [x] 17:00~23:00 저녁식사 및 휴식



## ✨ 오늘 배운 내용

- PT면접 & 실무면접



## 👀 수행한 업무 및 작성한 코드

- << 파이썬 알고리즘 인터뷰 >>

```python
"""MST : kruskal"""
# N, K = 4, 2
# edges = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
# edges.sort(key=lambda x: x[2], reverse=True)

# # find_set
# p = [i for i in range(N + 1)]
# def find_set(v):
#     if v != p[v]:
#         p[v] = find_set(p[v])
#     return p[v]

# # kruskal
# ans = cnt = 0
# while cnt < N - 1:
#     u, v, w = edges.pop()
#     a, b = find_set(u), find_set(v)
#     if a == b: continue
#     p[b] = a
#     cnt += 1
#     ans += w

# print(ans)

"""Dijkstra"""
import heapq
N, K = 4, 2
G = [[] for _ in range(N + 1)]
info = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
for u, v, w in info:
    G[u].append((v, w))
dist = [float('inf')] * (N + 1)

def dijkstra(start):
    Q = []
    heapq.heappush(Q, (0, start))
    dist[start] = 0

    while Q:
        d, u = heapq.heappop(Q)
        if dist[u] < d: continue

        for v, w in G[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(Q, (dist[v], v))

dijkstra(K)
ans = max(dist[1:])
if ans == float('inf'):
    print(-1)
else:
    print(ans)
```





## 🐱‍💻 아쉬운 점 & 느낀 점

- PT면접과 실무면접
- 부족한 부분이 많다는 생각이 들었습니다...

 

