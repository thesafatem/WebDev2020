a = int(input())
cnt = 0
while a != 0:
    cnt = cnt + a % 2
    a = a // 2
if (cnt == 1):
    print("YES")
else:
    print("NO")