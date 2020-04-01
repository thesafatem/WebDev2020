a = int(input())
b = int(input())
a = a + a % 2
while a <= b:
    print(a, end = " ")
    a += 2
    