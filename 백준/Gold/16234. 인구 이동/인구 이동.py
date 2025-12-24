from collections import deque

N, L, R = map(int, input().split())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
result = 0


def bfs(x, y, index):
    temp = []  # 연결된 나라
    temp.append((x, y))
    q = deque()
    q.append((x, y))
    u[x][y] = index
    total = arr[x][y]
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dxdy[i][0]
            ny = y + dxdy[i][1]
            if 0 <= nx < N and 0 <= ny < N and u[nx][ny] == -1:
                if L <= abs(arr[nx][ny] - arr[x][y]) <= R:
                    q.append((nx, ny))
                    u[nx][ny] = index
                    total += arr[nx][ny]
                    cnt += 1
                    temp.append((nx, ny))

    for i, j in temp:
        arr[i][j] = total // cnt


t = 0

while True:
    u = [[-1] * N for _ in range(N)]  # 하루다시 시작
    index = 0
    for i in range(N):
        for j in range(N):
            if u[i][j] == -1:
                bfs(i, j, index)
                index += 1

    if index == N * N:
        break
    t += 1

print(t)
