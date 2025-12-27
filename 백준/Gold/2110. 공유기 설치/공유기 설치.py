n, c = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()  # 이진탐색 할려면

start = 1 #최소거리
end = arr[len(arr)-1] - arr[0] #최대
result = 0

while start <= end:
    mid = (start + end) // 2 #거리찾고
    temp = arr[0]  # 최대한 많이 설치하고 싶다면, 가장 왼쪽 가능한 위치에 먼저 설치하는 것이 항상 이득
    cnt = 1
    for i in range(1, n): #공유기 설치
        if arr[i] >= temp + mid:
            temp = arr[i]
            cnt += 1

    if cnt>=c: #만약 C보다 더 설치했으면 거리 증가시키기위해 
        start = mid +1 #오른쪽 을본다
        result = mid
    else:
        end = mid -1 #왼쪽을 본다


print(result)

