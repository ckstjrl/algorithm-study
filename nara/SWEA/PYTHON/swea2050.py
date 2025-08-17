txt = input()
for x in txt:
    print(ord(x) - ord('A') + 1, end=' ')