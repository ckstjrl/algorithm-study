#D1: boj2864 5와 6의 차이

#숫자 받기
A, B = input().split()

# 문자열 변환
low_A = ''
high_A = ''

for i in range(len(A)):
    if A[i] == '6':
        # 최솟값: 6을 5로
        low_A += '5'
    else:
        low_A += A[i]
    
    if A[i] == '5':
        # 최댓값: 5를 6으로
        high_A += '6'
    else:
        high_A += A[i]

low_B = ''
high_B = ''

for i in range(len(B)):
    if B[i] == '6':
        low_B += '5'
    else:
        low_B += B[i]
    
    if B[i] == '5':
        high_B += '6'
    else:
        high_B += B[i]

low_num = int(low_A) + int(low_B)

high_num = int(high_A) + int(high_B)

print(low_num, high_num)