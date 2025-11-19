#BOJ1075 나누기

# 1) N을 F로 나누어 떨어지게 만드는 동시에 2) 마지막 두 자리를 가능한 가장 작은 수로 만들려는 게 목적
# 두 가지 목적을 동시에 충족시켜야 했던 문제

N = input().strip()

F = input().strip()

# 마지막 두 자리를 출력해줘야 하기 때문에 우선 해당 두 자리를 먼저 받아오고 시작
ans = str(N[-2]) + str(N[-1])

left = int(N) % int(F)

add_num = int(F) - left

# 가능한 옵션 1) 나머지를 두 자리에 더해주는 경우
ans_1 = int(ans) - left

# 최소값을 만들어야 하기 때문에 가능하다면 나눠야 하는 수를 반복적으로 빼준다, 0보다 큰 경우
while (ans_1 - int(F)) >= 0:
    ans_1 = ans_1 - int(F)

# 가능한 옵션 2) 나누는 수에서 나머지를 뺀 값을 두 자리에 더해주는 경우
ans_2 = int(ans) + add_num

# 최소값을 만들어야 하기 때문에 가능하다면 나눠야 하는 수를 반복적으로 빼준다, 0보다 큰 경우
while (ans_2 - int(F)) >= 0:
    ans_2 = ans_2 - int(F)

# 둘 중 더 작은 수를 답으로 결정
if ans_1 < 0:
    ans = ans_2
else:
    ans = ans_1

# 만약 답이 한자리 수가 된다면 십의 자리에 0을 붙여주기
if ans < 10:
    ans = '0' + str(ans)

print(ans)