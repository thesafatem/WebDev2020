n = int(input())
a = list(map(int, input().strip().split()))
for i in range(0, n, 2):
    print(a[i], end = " ")