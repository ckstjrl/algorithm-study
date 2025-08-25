A, B, V = map(int, input().split())
d = (V-B-1)//(A-B) + 1  # 올림 처리를 위해 분자에 -1

print(d)