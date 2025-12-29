n = int(input())
arr = list(map(int, input().split()))
arr.reverse()
dp = [1] * n #자기자신은 증가하는길이 1이다
for i in range(1, n):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(len(arr) -max(dp))