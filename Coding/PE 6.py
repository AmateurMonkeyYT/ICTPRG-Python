n = 1
a = 0
natSq = 0
sumSq = 0

for n in range (1,101):
    natSq = n ** 2 + natSq
for n in range (1,101):
    a += n
sumSq = a ** 2
print(sumSq - natSq)