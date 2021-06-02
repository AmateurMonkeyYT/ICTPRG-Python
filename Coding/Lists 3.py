maxN = 0
total = 0
count = 0

for x in [89, 456, 4, 55, 232, 2, 54, 78, 65, 45, 12, 459, 35616, 45 ,78]:
    total += x
    if (x > maxN):
        maxN = x
    count += 1
print(total)
print(total / count)
print(maxN)