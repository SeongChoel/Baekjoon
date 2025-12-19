def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        elif stuff == 1:
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            return False

    return True


def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        x, y, stuff, operate = frame  # x,y, 구조물, 설치여부
        if operate == 0:  # 삭제
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])
        elif operate == 1:
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])
    return sorted(answer)


print(solution(5, [[1, 0, 0, 1],
                   [1, 1, 1, 1],
                   [2, 1, 0, 1],
                   [2, 2, 1, 1],
                   [5, 0, 0, 1],
                   [5, 1, 0, 1],
                   [4, 2, 1, 1],
                   [3, 2, 1, 1]]))
