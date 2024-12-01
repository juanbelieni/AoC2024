xs, ys = [], []

while (line := input()) != "":
    x, y = map(int, line.split())
    xs.append(x)
    ys.append(y)

xs = sorted(xs)
ys = sorted(ys)

n = sum([abs(y - x) for x, y in zip(xs, ys)])
print(n)
