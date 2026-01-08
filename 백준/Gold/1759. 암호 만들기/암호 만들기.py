from itertools import combinations

L, C = map(int, input().split())

arr = list(input().split())

arr.sort()
result = []
for i in combinations(arr, L):
    mo_cnt = 0
    ja_cnt = 0
    for j in i:
        if j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u':
            mo_cnt += 1
        else:
            ja_cnt += 1

    if mo_cnt >= 1 and ja_cnt>=2:
        result.append(i)

for i in result:
    for j in i:
        print(j,end="")
    print()

