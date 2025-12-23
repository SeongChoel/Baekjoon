from itertools import combinations

n = int(input())
arr = []
teacher = []
ex = []

for i in range(n):
    arr.append(input().split())

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'T':
            teacher.append((i, j))
        if arr[i][j] == 'X':
            ex.append((i, j))


def func(x, y, direction):  # 검사
    if direction == 0:
        while True:
            if y < 0: break
            if arr[x][y] == 'S': return True
            if arr[x][y] == 'O': return False
            y -= 1
    if direction == 1:
        while True:
            if y >= n: break
            if arr[x][y] == 'S': return True
            if arr[x][y] == 'O': return False
            y += 1
    if direction == 2:
        while True:
            if x < 0: break
            if arr[x][y] == 'S': return True
            if arr[x][y] == 'O': return False
            x -= 1
    if direction == 3:
        while True:
            if x >= n: break
            if arr[x][y] == 'S': return True
            if arr[x][y] == 'O': return False
            x += 1

    return False

find = False
for comb in combinations(ex, 3):  # X인 공간에서 3개의 모든 조합
    for x, y in comb:  # 조합 좌표 꺼내서
        arr[x][y] = 'O'

    detected = False

    for x, y in teacher:  # 선생님 좌표 꺼내서
        for i in range(4):  # 상하좌우
            if func(x, y, i): #학생찾음
                detected = True #찾음
                break

    for x, y in comb:
        arr[x][y] = 'X'

    if detected:
        find = False
    else:
        find = True
        break

if find:
    print('YES')
else: #못찾으면
    print("NO")
