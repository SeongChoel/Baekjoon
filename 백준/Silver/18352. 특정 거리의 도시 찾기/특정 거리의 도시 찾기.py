from collections import deque
import sys
input = sys.stdin.readline


n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
result = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
distance = [-1] * (n + 1)  # 최단거리구하는 리스트
distance[x] = 0  # 출발도시는 0
q = deque([x])
while q:
    now = q.popleft()
    for i in graph[now]:
        if distance[i] == -1:
            distance[i] = distance[now] + 1
            q.append(i)

for i in range(1,n+1):
    if distance[i]== k:
        result.append(i)

if len(result) == 0:
    print(-1)
else:
    for i in range(len(result)):
        print(result[i])

