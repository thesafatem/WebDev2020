n = int(input())
a = list(map(int, input().strip().split()))
if n < 3:
    print(0)
    exit()
cnt = 0
for i in range (1, n - 1):
    cnt = cnt + int(a[i - 1] < a[i] and a[i + 1] < a[i])
print(cnt)