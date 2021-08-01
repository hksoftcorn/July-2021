# Dynamic Programming

### 1. 1로 만들기

```python
N = int(input())
dp = [0] * 1000001
""" dp - 메모이제이션
def calc(n):
    if n == 1: return 0 
    if dp[n]: return dp[n]
    dp[n] = calc(n - 1) + 1

    if n % 3 == 0:
        dp[n] = min(dp[n], calc(n // 3) + 1)
    elif n % 2 == 0:
        dp[n] = min(dp[n], calc(n // 2) + 1)
    return calc(n)

print(calc(N))
"""
# 타뷸레이션
dp[0] = 10000001
dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, N + 1):
    a = 0; b = 0
    if i % 3 == 0:
        a = i // 3
    if i % 2 == 0:
        b = i // 2

    dp[i] = min(dp[i - 1] + 1, dp[a] + 1, dp[b] + 1)

print(dp[N])
```

- 메모이제이션
- 타뷸레이션

### 2. 2n 타일링

```python
n = int(input())
dp = [0] * 10000000
dp[1] = 1
dp[2] = 2
def tile(n):
    if n <= 2:
        return dp[n]
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
print(tile(n) % 10007)
```

### 3. 계단 오르기

```python
n = int(input()) # 1 <= n <= 300
steps = [0] + [int(input()) for _ in range(n)]
# print(steps)
memo = [0] * (n + 1)

def dp(n):
    if n == 1:
        return steps[1]
    elif n == 2:
        return steps[1] + steps[2]
    elif n == 3:
        return max(steps[1] + steps[3], steps[2] + steps[3])
    else:
        memo[1] = steps[1]
        memo[2] = steps[1] + steps[2]
        memo[3] = max(steps[1] + steps[3], steps[2] + steps[3])
        for i in range(4, n + 1):
            memo[i] = max(memo[i - 2] + steps[i], memo[i - 3] + steps[i - 1] + steps[i])
        return memo[n]
print(dp(n)) 
```

### 4. 123더하기

```python
def dp(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return dp(n - 1) + dp(n - 2) + dp(n - 3)

for tc in range(int(input())):
    # n <= 12
    n = int(input())
    print(dp(n))
```

