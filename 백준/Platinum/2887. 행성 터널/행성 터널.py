def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

x = []
y = []
z = []
for i in range(1, n + 1):
    t = list(map(int, input().split()))
    x.append((t[0], i))
    y.append((t[1], i))
    z.append((t[2], i))

x.sort()
y.sort()
z.sort()
e = []
for i in range(n - 1):
    e.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
    e.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    e.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

e.sort()
result = 0
for i in e:
    cost, a, b = i
    if find(parent,a) != find(parent,b):
        union(parent,a,b)
        result +=cost

print(result)

