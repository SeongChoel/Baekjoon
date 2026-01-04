from collections import deque

n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))
x, y = 0, 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x, y = i, j
            graph[x][y] = 0
            break
shark = 2
result = 0
cnt = 0
dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs():  # 현재 위치에서 다른 모든위치 최단거리 계산
    dist = [[-1] * n for _ in range(n)]  # 일단 다 도달할수없음
    q = deque()
    q.append((x, y))
    dist[x][y] = 0 #자기자신은 0
    while q:
        xx, yy = q.popleft()
        for i in range(4):
            nx = xx + dxdy[i][0]
            ny = yy + dxdy[i][1]
            if 0 <= nx < n and 0 <= ny < n:
                # 자신의 크기보다 작거나 같아야지 지나갈수있음
                if dist[nx][ny] == -1 and graph[nx][ny] <= shark: #위치들이 업데이트 안되었고, 자기자신 보다 작거나 같을때
                    dist[nx][ny] = dist[xx][yy] + 1
                    q.append((nx, ny))
    return dist  # 현재 위치에서 bfs를 실행했을때 모든위치의 최단거리가 나옴


def find(dist):  # 최단거리나온 값과, 물고기를 찾을 함수
    a, b = 0, 0
    min_d = 1e9
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= graph[i][j] < shark:  # 도달이 가능하면서 물고기가 조건이 성립
                if dist[i][j] < min_d:  # 가장 가까운 물고기 한 마리만 선택
                    a, b = i, j
                    min_d = dist[i][j]  # 이렇게 돌면 문제 조건에서 맨 왼쪽 위와 같다.. for문을 그냥 원래대로 돌면
    if min_d == 1e9:
        return None
    else:
        return a, b, min_d  # 먹을 물고기의 위치와 최단거리


while True:
    value = find(bfs())

    if value is None:
        print(result)
        break
    else:
        x, y = value[0], value[1]
        result += value[2]
        graph[x][y] = 0 #먹은 물고기는 0으로
        cnt += 1
        if cnt >= shark:
            shark += 1
            cnt = 0
