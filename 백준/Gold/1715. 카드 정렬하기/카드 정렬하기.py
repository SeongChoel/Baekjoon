import heapq

n = int(input())
result = 0
h = []
for i in range(n):
    a = int(input())
    heapq.heappush(h, a)

while len(h) != 1:
    x = heapq.heappop(h)
    y = heapq.heappop(h)
    result += x+y
    heapq.heappush(h,x+y)

print(result)
