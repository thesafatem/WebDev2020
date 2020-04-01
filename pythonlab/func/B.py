def binpow(a, p):
    if (p == 0):
        return 1
    elif (p % 2 == 0):
        res = binpow(a, p // 2)
        return res * res
    else:
        return a * binpow(a, p - 1)

s = input().split()
a = float(s[0])
p = int(s[1])
print(binpow(a, p))