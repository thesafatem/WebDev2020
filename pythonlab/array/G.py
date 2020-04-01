n = int(input())
a = list(map(int, input().strip().split()))
for i in range(n // 2):
    temp = a[n - 1 - i]
    a[n - 1 - i] = a[i]
    a[i] = temp
for i in range(n):
    print(a[i], end = " ")