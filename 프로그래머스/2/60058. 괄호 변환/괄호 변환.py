def func(p):
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


def solution(p):
    answer = ""

    if p == "":
        return ""

    if func(p):
        return p

    # 위에 조건 2개가 아닐때 즉 올바른 괄호 문자열이 아니라면
    index = check(p)
    u = p[:index + 1]
    v = p[index + 1:]

    if func(u):
        return u + solution(v)

    else:
        answer = "("
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('

        answer += "".join(u)

    return answer


print(solution("()))((()"))
