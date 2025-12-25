# boj 2810. 컵홀더
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

# 컵홀더 끼워넣기
seats = input().replace('S', '*S*').replace('LL', '*LL*').replace('**', '*')

ans = seats.count('*')

# 정답 인원 수가 좌석 수를 넘을 수 없음
print(min(ans, n))

