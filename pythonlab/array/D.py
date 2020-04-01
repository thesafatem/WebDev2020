n = int(input())
a = list(map(int, input().strip().split()))
cnt = 0
if n == 1:
    print(0)
    exit()
for i in range(1, n):
    cnt = cnt + int(a[i] > a[i - 1])
print(cnt)