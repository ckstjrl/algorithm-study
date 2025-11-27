# BOJ 1075. 나누기 (D1 /B2)
# https://www.acmicpc.net/problem/1075

n = input()
# 뒤 2자리 00으로 초기화
n = int(n[:-2] + '00')

f = int(input())

#00부터 99까지 확인하기
for i in range(100):
    if n%f == 0:
        print(f"{n%100:02d}")
        break
    n += 1