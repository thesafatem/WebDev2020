a = int(input())
i = 1
cnt = 0
while i * i <= a:
    if (i * i == a):
        cnt = cnt + 1
    elif a % i  == 0:
        cnt = cnt + 2
    i = i + 1
print(cnt)