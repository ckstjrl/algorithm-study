# BOJ 1712. 손익분기점 (D1 / B2)
# https://www.acmicpc.net/problem/1712


# 손익분기점 = 고정비용 / (판매가격 - 가변비용)
# 손익분기점 이후부터 이익 발생

# 고정비용, 가변비용, 판매가격
a, b, c = map(int, input().split())  
if b >= c:
    print(-1)
else:
    print(a // (c - b) + 1)
