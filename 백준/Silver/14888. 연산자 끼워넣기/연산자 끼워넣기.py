n = int(input())
arr = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

maxV = -1e9 -1
minV = 1e9 +1


def dfs(i, now):
    global minV, maxV, add, sub, mul, div

    if i == n:  # 모든 연산자를 다 사용한 경우
        minV = min(minV, now)
        maxV = max(maxV, now)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, now + arr[i])
            add += 1  # 백트래킹
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - arr[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * arr[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / arr[i]))
            div += 1


dfs(1, arr[0])  # 다음인덱스, 현재수의합

print(maxV)
print(minV)
