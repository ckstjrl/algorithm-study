N = input()
l = len(N) - 1
res = 0
for i in range(l, -1, -1):
    if N[i] == 'A':
        res += 10 * (16 ** (l - i))
    elif N[i] == 'B':
        res += 11 * (16 ** (l - i))
    elif N[i] == 'C':
        res += 12 * (16 ** (l - i))
    elif N[i] == 'D':
        res += 13 * (16 ** (l - i))
    elif N[i] == 'E':
        res += 14 * (16 ** (l - i))
    elif N[i] == 'F':
        res += 15 * (16 ** (l - i))
    else:
        res += int(N[i]) * (16 ** (l - i))
print(res)