import math
x1, y1 = [float(x) for x in input().strip().split()]
x2, y2 = [float(x) for x in input().strip().split()]
print('{:.4f}'.format(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)))