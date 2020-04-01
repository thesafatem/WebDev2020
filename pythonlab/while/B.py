a = int(input())
i = 2
while i * i <= a:
    if a % i == 0:
        break
    i = i + 1
if a % i == 0:
    print(i)
else:
    print(a)