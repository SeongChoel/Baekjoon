import sys
input = sys.stdin.readline
n, m = map(int, input().split())

arr = []
temp = [[0] * m for _ in range(n)]  # 벽을 설치한 뒤의 맵

for i in range(n):
    arr.append(list(map(int, input().split())))

dxdy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
result = 0


def virus(x, y):  # dfs을 이용
    for i in range(4):
        nx = x + dxdy[i][0]
        ny = y + dxdy[i][1]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)


def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score


def dfs(count):  # dfs로 울타리 설치 -> 안전 영역 계산
    global result

    if count == 3:  # 벽을 3개 설치했을때
        for i in range(n):
            for j in range(m):
                temp[i][j] = arr[i][j]  # 현재 지도를 복사
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:  # 바이러스 위치에서 전파
                    virus(i, j)
        result = max(result, get_score())
        return

    # 벽을 설치하는 과정
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1  # 벽설치
                count += 1
                dfs(count)  # 다음 벽 설치
                arr[i][j] = 0  # 벽제거
                count -= 1


dfs(0)
print(result)
