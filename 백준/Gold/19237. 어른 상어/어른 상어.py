n, m, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 1,2,3,4는  위,아래,왼쪽,오른쪽 나중에 인덱스로 0,1,2,3활용
dd = list(map(int, input().split())) #각 상어의 방향
smell = [[[0, 0]] * n for _ in range(n)]  # (상어번호, 남은 시간)확인하는 리스트, arr과 따로 관리

time = 0
priority = []
for i in range(m):
    temp = []
    for j in range(4):
        row = list(map(int, input().split()))
        temp.append(row)
    priority.append(temp)

def smell_update():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] > 0:  # 냄새가 있는경우
                smell[i][j][1] -= 1
            if arr[i][j] != 0:  # 상어위치로 냄새 조정
                smell[i][j] = [arr[i][j], k]  # 상어번호, k


def shark_move():
    new = [[0] * n for _ in range(n)] #상어 이동 결과
    for x in range(n):
        for y in range(n):
            if arr[x][y] != 0:  # 상어존재
                direction = dd[arr[x][y] - 1]  # 상어 숫자가 1이면 dd에서는 0으로 찾아야함 -> 1,2,3,4로나옴
                found = False
                for idx in range(4):  # 상하좌우 확인(냄새없는 위치 찾기)
                    nx = x + dxdy[priority[arr[x][y] - 1][direction - 1][idx] - 1][0]  # 번호가 1이면 0으로 환산, 방향도 -1해줘야함, 인덱스 4번반복, 마지막 -1은 방향 번호(1~4)를 dx, dy 인덱스(0~3)로 변환
                    ny = y + dxdy[priority[arr[x][y] - 1][direction - 1][idx] - 1][1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][1] == 0:  # 냄새가 없음
                            dd[arr[x][y] - 1] = priority[arr[x][y] - 1][direction - 1][idx]  # 상어방향 바꿈
                            if new[nx][ny] == 0: #이동
                                new[nx][ny] = arr[x][y]
                            else: #상어가 있으면 (작은번호)
                                new[nx][ny] = min(new[nx][ny],arr[x][y])
                            found = True
                            break #이게 만약 냄새 없는데가 한칸이면 거기로 가고 바로 break
                if found: #냄새없는 위치 찾았으면 밑에 코드 실행 안해도됌
                    continue
                #밑에는 이제 자신의 냄새로
                for idx in range(4):
                    nx = x + dxdy[priority[arr[x][y]-1][direction-1][idx]-1][0]
                    ny = y + dxdy[priority[arr[x][y]-1][direction-1][idx]-1][1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][0] == arr[x][y]: #자기 냄새
                            dd[arr[x][y]-1] =priority[arr[x][y]-1][direction-1][idx]
                            new[nx][ny] = arr[x][y] #이동
                            break

    return new

while True:
    smell_update()
    new = shark_move()
    arr = new
    time += 1

    flags = True
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 1:
                flags = False

    if flags:
        print(time)
        break

    if time >= 1000:
        print(-1)
        break
