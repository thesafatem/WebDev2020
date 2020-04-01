def min2(a, b):
    return a if a <= b else b

def min4(a, b, c, d):
    a = min2(a, b)
    b = min2(c, d)
    return min2(a, b)

a = list(map(int, input().strip().split()))
print(min4(a[0], a[1], a[2], a[3]))
