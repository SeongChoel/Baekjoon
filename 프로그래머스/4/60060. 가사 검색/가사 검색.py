from bisect import bisect_right, bisect_left


def count_range(a, left_value, right_value):
    left = bisect_left(a, left_value)
    right = bisect_right(a, right_value)
    return right - left


arr = [[] for i in range(10001)]
arr2 = [[] for i in range(10001)]


def solution(words, queries):
    result = []
    for w in words:
        arr[len(w)].append(w)
        arr2[len(w)].append(w[::-1])

    for i in range(10001):
        arr[i].sort()
        arr2[i].sort()

    for q in queries:
        if q[0] != "?":  # 접미사일떄
            temp = count_range(arr[len(q)], q.replace('?', ''), q.replace('?', '')+chr(255))
        else:  # 접두사일때
            temp = count_range(arr2[len(q)], q[::-1].replace("?", ''), q[::-1].replace('?', '')+chr(255))
        result.append(temp)
    return result

