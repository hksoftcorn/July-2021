# 업무일지

### ✔ Summary

- [x] 09:00~13:00 APS
- [x] 17:30~24:00 Vue3 - TODO, Infinity scroll



## ✨ 오늘 배운 내용

- [Vue.js](./vuejs/TIPs.md)




## 👀 수행한 업무 및 작성한 코드

```python
# import pprint
N, W = map(int, input().split())
dp = [[0] * (W + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    weight, value = map(int, input().split())
    for j in range(1, W + 1):
        if weight > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i -1][j - weight] + value)

# pprint.pprint(dp)
print(dp[N][W])
```





## 🐱‍💻 아쉬운 점 & 느낀 점

- Vue 3로 바꾸어서 해봅시다.
- UX/UI 기초 설계

 

