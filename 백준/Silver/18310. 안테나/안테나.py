n = int(input())

arr = list(map(int, input().split()))
arr.sort()

if len(arr)%2==0:
    mid = arr[(len(arr)//2)-1]
else:
    mid = arr[(len(arr)//2)]

print(mid)


