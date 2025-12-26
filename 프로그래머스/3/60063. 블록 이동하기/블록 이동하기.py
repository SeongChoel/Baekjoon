from collections import deque

def next_pos(pos, board):
    temp = [] #이동한 위치들 담는 리스트
    pos = list(pos)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    dxdy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for i in range(4): #위치이동 시작점 4개의 좌표를 다 봐야함
        pos1_next_x, post1_next_y, post2_next_x, post2_next_y = pos1_x + dxdy[i][0], pos1_y + dxdy[i][1], pos2_x + dxdy[i][0], pos2_y + dxdy[i][1]
        if board[pos1_next_x][post1_next_y] == 0 and board[post2_next_x][post2_next_y] == 0:
            temp.append({(pos1_next_x, post1_next_y), (post2_next_x, post2_next_y)})

    if pos1_x == pos2_x: #가로
        for i in [-1,1]: #위, 아래
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:  # -1 위, 1 아래쪽 비어있다면
                temp.append({(pos1_x,pos1_y),(pos1_x+i,pos1_y)}) #회전 축 2개, 가능한 모든경우 넣기
                temp.append({(pos2_x,pos2_y),(pos2_x+i,pos2_y)})

    if pos1_y == pos2_y: #세로
        for i in [-1, 1]:  # 왼쪽, 오른쪽
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0:  # 왼쪽 혹은 오른쪽 두 칸이 모두 비어 있다면
                temp.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)}) #가능한 모든 경우 넣기
                temp.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})

    return temp #현재 위치에서 이동할수 있는 위치 반환


def solution(board):
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]  # 업데이트

    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)}
    q.append((pos, 0))
    visited.append(pos)

    while q:
        pos, num = q.popleft()
        if (n, n) in pos:
            return num

        for i in next_pos(pos, new_board):
            if i not in visited:
                q.append((i, num + 1))
                visited.append(i)
    return 0

