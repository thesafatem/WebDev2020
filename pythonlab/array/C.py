n = int(input())
a = list(map(int, input().strip().split()))
cnt = 0
for i in range(n):
    cnt = cnt + int(a[i] > 0)
print(cnt)