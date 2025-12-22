def func(p):  # 올바른 괄호 문자열
    cnt = 0
    for i in p:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    if cnt == 0:
        return True
    return False


def check(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return i
    return None


def solution(p):
    answer = ""

    if p == "":
        return ""

    # 분리
    index = check(p)
    u = p[:index + 1]
    v = p[index + 1:]

    if func(u):
        return u + solution(v)
    else:
        answer += "("
        answer += solution(v)
        answer += ")"

        temp_u = ""
        for i in range(1, len(u) - 1):
            temp_u += u[i]

        temp_uu = ""

        for i in temp_u:
            if i == ")":
                temp_uu += "("
            else:
                temp_uu += ")"

        answer += temp_uu

        return answer


