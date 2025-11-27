a, b, c, d, e, f = map(int, input().split())
x = int(((c * e) - (b * f)) // ((a * e) - (b * d)))
y = int(((c * d) - (a * f)) // ((b * d) - (a * e)))
print(x, y)