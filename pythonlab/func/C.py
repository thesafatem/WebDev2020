def xor(a, b):
    return (a or b) and (not a or not b)

a = list(map(int, input().strip().split()))
print(int(xor(bool(a[0]), bool(a[1]))))