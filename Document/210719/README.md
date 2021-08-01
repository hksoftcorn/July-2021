# 업무일지

### ✔ Summary

- [x] 09:00~18:00 기능 명세 / UI 설계 feat. Figma
- [x] 21:00~23:00 알고리즘 풀이 ~~& JIRA 연동~~

- [x] 23:00~02:00 국민은행 면접준비 ㅎㅅㅎ



## ✨ 오늘 배운 내용

- [REST API](./REST/REST.md)

  `HTTP URI(Uniform Resource Identifier)`를 통해 자원(Resource)을 명시하고, `HTTP Method(POST, GET, PUT, DELETE)`를 통해 해당 자원에 대한 CRUD Operation을 적용하는 것을 의미한다.

- [APS - heapq & 다익스트라 & 벨만-포드](./APS/APS.md)



## 👀 수행한 업무 및 작성한 코드

- Figma 화면 설계
- APS - 다익스트라 & 벨만-포드

```python
import heapq

V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))

dist = [float('inf')] * (V + 1)

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

dijkstra(1)
print(dist[V])
```



## 🐱‍💻 아쉬운 점 & 느낀 점

- bellman-ford 개념에 대한 이해가 더욱 필요
- 1865_웜홀 문제 해결 못함..

