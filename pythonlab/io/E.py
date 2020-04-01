v = int(input())
t = int(input())
if v < 0:
    v = (109 - abs(v) * t % 109) % 109
else:
    v = v * t % 109
print(v)