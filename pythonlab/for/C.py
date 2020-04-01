a = int(input())
b = int(input())
q = 0
while q * q <= b:
    if (q * q >= a):
        print(q * q, end = " ")
    q = q + 1