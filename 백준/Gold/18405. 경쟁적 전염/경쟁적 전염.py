from collections import deque

n, k = map(int, input().split())

arr = []  # 전체
temp = []  # 바이러스 정보

for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            temp.append((arr[i][j], 0, i, j))  # 바이러스 종류, 시간, x, y

temp.sort()
q = deque()
for x in temp:
    q.append(x)

s, x, y = map(int, input().split())
dxdy = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 위 -오른 - 밑 - 왼

while q:
    a, b, c, d = q.popleft()  # 바이러스, 시간, x, y
    if b == s:
        break
    for i in range(4):
        nx = c + dxdy[i][0]
        ny = d + dxdy[i][1]
        if 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] == 0:
                arr[nx][ny] = a
                q.append((a, b + 1, nx, ny))

print(arr[x - 1][y - 1])
