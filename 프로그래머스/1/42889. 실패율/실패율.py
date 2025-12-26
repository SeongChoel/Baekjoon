def solution(N, stages):
    answer = []

    for i in range(1, N + 1):
        parent = 0
        child = 0
        for j in stages:
            if i <= j:
                parent += 1
            if i == j:
                child += 1
        if parent == 0:
            total = 0
        else:
            total = child / parent
        answer.append((total, i))
    answer.sort(key=lambda x: (-x[0],x[1]) )

    answer2 = [i[1] for i in answer]

    return answer2