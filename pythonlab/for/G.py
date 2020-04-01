a = int(input())
div = 2
while div * div <= a:
    if a % div == 0:
        break
    div = div + 1
if a % div == 0:
    print(div)
else:
    print(a)