from collections import deque
def solution(n):
    # 오른쪽, 아래, 왼쪽, 위
    directions = deque([(0, 1), (1, 0), (0, -1), (-1, 0)])
    answer = [[0 for _ in range(n)] for _ in range(n)]
    row, col = 0, 0
    number = 1

    while number <= n * n:
        answer[row][col] = number
        # 다음 위치가 유효한 지ㄷ
        if 0 <= row + directions[0][0] < n and 0 <= col + directions[0][1] < n:
            if answer[row + directions[0][0]][col + directions[0][1]] != 0:
                directions.rotate(-1)
        else:
            directions.rotate(-1)

        row += directions[0][0]
        col += directions[0][1]
        number += 1

    return answer
