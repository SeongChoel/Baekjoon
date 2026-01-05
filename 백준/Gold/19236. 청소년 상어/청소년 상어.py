import copy

dxdy = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
arr = []

for _ in range(4):
    t = list(map(int, input().split()))
    row = []
    for i in range(0, 8, 2):
        row.append([t[i], t[i + 1] - 1])  # 물고기, 방향(0부터시작)
    arr.append(row)


# dxdy가 시계방향이면 (i+1)%8은 but dxdy가 반시계
def turn_left(direction):
    return (direction + 1) % 8


def find_fish(arr, index):  # 특정 번호 물고기 위치리턴
    for i in range(4):
        for j in range(4):
            if arr[i][j][0] == index:
                return i, j
    return None


def move_fish(arr, x, y):
    for i in range(1, 17):
        position = find_fish(arr, i)
        if position != None:
            a, b = position[0], position[1]
            direction = arr[a][b][1]
            for j in range(8):  # j를 이용해서 8가지를 다 도는게 아니라 그 해당하는 direction으로 가야함
                nx = a + dxdy[direction][0]
                ny = b + dxdy[direction][1]
                if 0 <= nx < 4 and 0 <= ny < 4:
                    if not (nx == x and ny == y):
                        arr[a][b][1] = direction  # 방향 바꾼거
                        arr[a][b], arr[nx][ny] = arr[nx][ny], arr[a][b]
                        break
                direction = turn_left(direction)  # 조건 부합하지 않으면 45도 회전


def get_eat(arr, x, y):  # 상어가 먹을수있는 물고기 위치반환
    position = []
    direction = arr[x][y][1]

    for i in range(4):
        x += dxdy[direction][0]
        y += dxdy[direction][1]
        if 0 <= x < 4 and 0 <= y < 4:
            if arr[x][y][0] != -1:
                position.append((x, y))

    return position


result = 0


def dfs(arr, x, y, total):
    global result
    arrt = copy.deepcopy(arr)  # 상태복사

    total += arrt[x][y][0]  # 물고기 먹기(선택)
    arrt[x][y][0] = -1  # 먹었으니 -1

    move_fish(arrt, x, y)  # 물고기이동(상태변화)

    p = get_eat(arrt, x, y)  # 상어이동, 위치찾기

    if len(p) == 0:  # 이동할 위치가없으면(종료조건)
        result = max(result, total)
        return

    for n_x, n_y in p:  # 재귀적으로 수행(선택)
        dfs(arrt, n_x, n_y, total)


dfs(arr, 0, 0, 0)
print(result)
