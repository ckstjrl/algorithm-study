H, M = map(int, input().split())
H = ((H - 1) + ((M + 15) // 60)) % 24
M = (M + 15) % 60
print(H, M)


