# X사: 1리터당 A엔
# Y사: 기본 B엔, C리터 이하라면 기본 요금. 넘는 경우 추가 요금, 1리터 마다 D엔.
# 한 달 사용량: P리터

ans = 0

#첫 줄: X사 1리터당 기본요금 A엔
A = int(input())

#둘째 줄: Y사 1리터당 기본요금 B엔
B = int(input())

#셋째 줄: Y사 기본요금 상한 C
C = int(input())

#넷째 줄: 1리터 당 추가요금 D
D = int(input())

#다섯째 줄: 한 달 사용 수도 양, P
P = int(input())

#최대한 싼 값을 찾기
# X사의 기본요금 기반 수도사용량
feeX = P * A

# Y사의 기본요금 기반 수도사용량
rest = P - C

if rest > 0:
    feeY =  B + (rest * D)
else:
    feeY = B

if feeX >= feeY:
    ans = feeY
else:
    ans = feeX

print(ans)