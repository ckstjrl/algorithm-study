# BOJ 30456. 바닥수 (D1 / B1)

# 바닥수 n, 자릿수 l
n, l = map(int, input().split())

# 자릿수-1만큼 1로 채우고, 마지막엔 n 넣기
ans = '1'*(l-1) + str(n)
print(ans)
