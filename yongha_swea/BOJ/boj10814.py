# BOJ10814 나이순 정렬

# 몇 번 사람이 나올지 우선 받기
N = int(input())

# input을 받고 나이 순서에 맞춰 다시 정리할 리스트
order_user = []

# N번에 걸쳐서 age, name을 하나의 리스트로 묶어서 다른 리스트에 넣어주기
for _ in range(N):
    age, name = map(str, input().split())
    order_user.append([int(age), name])

# 나이에 맞춰서 정렬 해주기
# 추가: 이름에 맞춰서 정렬하면 먼저 들어온 친구를 먼저 출력하는 것에 어긋남 따라서 오직 나이만 고려 조건이 되도록 해당 조건을 추가해준다
order_user.sort(key = lambda x: x[0])

for user in order_user:
    print(user[0], user[1])