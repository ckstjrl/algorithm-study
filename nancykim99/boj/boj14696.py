# A, B
# 별의 개수가 다를 시: 별이 많은 쪽 딱지가 이김
# 별의 개수가 같을 시: 동그라미 개수가 다를 시 : 동그라미가 많은 쪽 딱지가 이김
#     동그라미 개수가 같을 시: 네모의 개수가 다를 시 : 네모가 많은 쪽 딱지가 이김
#         네모의 개수가 같을 시 : 세모가 많은 쪽 딱지가 이김
#             세모의 개수까지 같다면 : 무승부 (D)

# 별 : 4
# 동그라미 : 3
# 네모 : 2
# 세모 : 1

# N : 딱지놀이의 총 라운드 수 / 1 <= N <= 1000
# a : A 딱지 내 그림 총 개수 / 1 <= a <= 100
# a개의 정수 : A 딱지 내 그림
# b : B 딱지 내 그림 총 개수 / 1 <= b <= 100
# b개의 정수 : B 딱지 내 그림

N = int(input())

for _ in range(N):
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))

    a = arr_a.pop(0)
    b = arr_b.pop(0)

    arr_a.sort(reverse=True)
    arr_b.sort(reverse=True)

    cnt_a = [0] * 4
    cnt_b = [0] * 4

    for i in range(len(arr_a)):
        if arr_a[i] == 4:
            cnt_a[0] += 1
        elif arr_a[i] == 3:
            cnt_a[1] += 1
        elif arr_a[i] == 2:
            cnt_a[2] += 1
        else:
            cnt_a[3] += 1

    for i in range(len(arr_b)):
        if arr_b[i] == 4:
            cnt_b[0] += 1
        elif arr_b[i] == 3:
            cnt_b[1] += 1
        elif arr_b[i] == 2:
            cnt_b[2] += 1
        else:
            cnt_b[3] += 1
    
    is_winner = False
    for i in range(4):
        if cnt_a[i] > cnt_b[i]:
            print('A')
            is_winner = True
            break
        elif cnt_a[i] < cnt_b[i]:
            print('B')
            is_winner = True
            break
    
    if not is_winner:
        print('D')