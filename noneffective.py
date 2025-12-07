import random
dbl1 = [random.randint(1, 2345), random.randint(1, 2345)]
dbl2 = [random.randint(1, 2345), random.randint(1, 2345)]
dbl3 = [random.randint(1, 2345), random.randint(1, 2345)]
dbl4 = [random.randint(1, 2345), random.randint(1, 2345)]
max1, max2, max3, max4 = max(dbl1), max(dbl2), max(dbl3), max(dbl4)
lusm = max1 + max2 + max3 + max4
for i in range(lusm, lusm - 5, -1):
    if i % 5 != 0:
        lusm = i
        break
print(lusm)
