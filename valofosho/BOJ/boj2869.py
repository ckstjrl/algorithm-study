import math
A, B, V = map(int, input().split())
# V-A 는 다음날 아침에 한 번에 올라갈 수 있는 경우의 수
# A-B는 올라갔다 내려가는 길이
ans = math.ceil((V-A) / (A-B)) + 1
print(ans)
