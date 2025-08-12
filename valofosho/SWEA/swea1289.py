T = int(input())
for test_case in range(1, T+1):
    arr = list(map(int, input()))
    cnt = 0
    prev = 0
    # 들어올 값을 기준으로 이전에 불린 값과 다르다면 수정이 필요
    # 1과 0에 상관없이 바뀌는 횟수에 영향을 받는다
    for digit in arr:
        if digit != prev:
            cnt += 1
            prev = digit
    print(f"#{test_case} {cnt}")

# 1차 답안
# T = int(input())
# for test_case in range(1, T+1):
#     arr = list(map(int, input()))
#     cnt = 0
#     prev = 0 # 이전 수와 다르면 변화가 필요하다
#     for digit in arr:
#         if digit == 1 and prev == 0:
#             cnt += 1
#             prev = 1
#         elif digit == 1 and prev == 1:
#             pass
#         elif digit == 0 and prev == 1:
#             cnt += 1
#             prev = 0
#     print(f"#{test_case} {cnt}")
