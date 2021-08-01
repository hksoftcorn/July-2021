# 업무일지

### ✔ Summary

```
09:00~09:40 [강의&미팅] PJT Review
			팔굽혀 피기(1/3)
09:40~10:00 [미팅] 팀미팅
			팔굽혀 피기(2/3)
10:10~12:00 [코드] FE 정리하기
			팔굽혀 피기(3/3)
			Lunch
13:00~13:50 [평가] 상호평가
14:00~17:30 [미팅] 팀미팅 - 기능 명세 및 아이디어 구체화
18:00~20:00 장보기
			Dinner
21:00~		취침
```



## ✨ 오늘 배운 내용

- [APS - 상호배타 집합들](./APS/APS.md)
- [공통PJT 리뷰](./PJT/README.md)



## 👀 수행한 업무 및 작성한 코드

- FE

- MST & 상호배타 집합들

```python
from collections import deque

N = int(input())
mi, mj = map(int, input().split()) # 정상 위치
arr = [list(map(int, input().split())) for _ in range(N)]
dist = [[0xfffffff] * N for _ in range(N)]

def bfs(v):
    r, c = v
    dist[r][c] = arr[r][c] ** 2
    Q = deque([(r, c)])
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def cal_cost(cur_r, cur_c, nr, nc):
        cur_ = arr[cur_r][cur_c]
        next_ = arr[nr][nc]

        if cur_ >= next_:
            return cur_ - next_
        else:
            return (next_ - cur_) ** 2

    while Q:
        cur_r, cur_c = Q.popleft()

        for i in range(4):
            nr, nc = cur_r + dr[i], cur_c + dc[i]
            # if 0 <= nr < N and 0 <= nc < N:
            if 0 > nr or nr >= N or 0 > nc or nc >= N: continue
            cost = cal_cost(cur_r, cur_c, nr, nc)
            if dist[nr][nc] > dist[cur_r][cur_c] + cost:
                dist[nr][nc] = dist[cur_r][cur_c] + cost
                Q.append((nr, nc))

for r in range(N):
    for c in range(N):
        if r == 0 or r == N or c == 0 or c == N:
            bfs((r, c))

print(dist[mi - 1][mj - 1])
```







## 🐱‍💻 아쉬운 점 & 느낀 점

- `힙`, `우선순위 큐`, `힙큐`  

- `다익스트라 힙큐` 활용 필요

  - 다익스트라 슈도코드를 보면서 했는데,
  - 2중 for 문으로 O(n^2) 으로 연산이 너무 많음
  - 따라서 다익스트라 힙큐를 활용하자

  
