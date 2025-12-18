n = int(input())

str_n = str(n)
left = 0
right = 0

for x in range(len(str_n)):
    if x< len(str_n)//2:
        left+= int(str_n[x])
    else:
        right +=int(str_n[x])

if left==right:
    print("LUCKY")
else:
    print("READY")
