# 2869. 달팽이는 올라가고 싶다

# 낮에 A미터 올라가고, 밤에 B미터 떨어지고, 나무 높이 V미터
A, B, V = map(int, input().split())

cnt = (V-A) // (A-B) + 1

if (V-A) % (A-B):
    cnt += 1

print(cnt)