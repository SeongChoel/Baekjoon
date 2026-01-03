from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    graph = [[False] * (n + 1) for _ in range(n + 1)]  # 인접행렬
    indegree = [0] * (n + 1)

    rank = list(map(int, input().split()))
    for i in range(n):  # 이게 제일 중요 방향그래프 간선 초기화(순위대로 ex 1위 - > 2위)
        for j in range(i + 1, n):
            graph[rank[i]][rank[j]] = True
            indegree[rank[j]] += 1

    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())  # a,b순서 상관없이 두개가 순위가 바꼈다는뜻으로 이해해야함

        if graph[a][b] == True:  # a->b였으면 b->a로
            graph[a][b] = False
            graph[b][a] = True
            indegree[b] -= 1
            indegree[a] += 1
        else:  # b->a였으면 a->b로
            graph[b][a] = False
            graph[a][b] = True
            indegree[a] -= 1
            indegree[b] += 1

    result = []
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    c = True
    cycle = False

    for i in range(n):
        if len(q) == 0:
            cycle = True
            break

        if len(q) >= 2:
            c = True
            break

        now = q.popleft()
        result.append(now)

        for j in range(1, n + 1):
            if graph[now][j] == True:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

    if not c:
        print("?")
    elif cycle:
        print("IMPOSSIBLE")
    else:
        for i in result:
            print(i, end=" ")
        print()
