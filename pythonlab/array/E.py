n = int(input())
a = list(map(int, input().strip().split()))
if n == 1:
    print("NO")
    exit()
for i in range(1, n):
    if (a[i] > 0) == (a[i - 1] > 0):
        print("YES")
        exit()
print("NO")