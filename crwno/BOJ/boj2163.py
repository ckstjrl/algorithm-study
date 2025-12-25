N, M = map(int, input().split())

cut = 0

piece = N
cut += N - 1

cut += piece * (M - 1)

print(cut)