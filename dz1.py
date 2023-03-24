a = int(input())
b = int(input())
c = int(input())

d = b * b - 4 * a * c

if d < 0:
    print("No roots")
elif d == 0:
    x = ((-1)*b) / (2*a)
    print("x = ", x)
else:
    x1 = ((-1)*b + pow(d, 0.5)) / (2*a)
    x2 = ((-1)*b - pow(d, 0.5)) / (2*a)
    print("x1 = ", x1)
    print("x2 = ", x2)
