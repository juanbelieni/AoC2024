from collections import defaultdict

xs = []
ys_count = defaultdict(lambda: 0)

while (line := input()) != "":
    x, y = map(int, line.split())
    xs.append(x)
    ys_count[y] += 1

n = sum([x * ys_count[x] for x in xs])
print(n)

