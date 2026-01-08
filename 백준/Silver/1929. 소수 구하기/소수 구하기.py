m, n = map(int, input().split())

arr = [True for i in range(1000001)]
arr[1] = False

for i in range(2, int(n ** 0.5) + 1):
    if arr[i]:
        j = 2
        while i * j <= n:
            arr[i * j] = False
            j += 1

for i in range(m, n + 1):
    if arr[i]:
        print(i)
