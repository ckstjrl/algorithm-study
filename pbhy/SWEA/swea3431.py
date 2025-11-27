# 3431. 준환이의 운동관리
'''
1주일에 L분 이상 U분 이하의 운동을 하여야 한다.
준환이는 이번 주에 X분만큼 운동을 하였다.

[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 세 정수 L, U, X(0≤ L ≤ U ≤ 107, 0 ≤ X ≤ 107)가 공백으로 구분되어 주어진다.

[출력]

각 테스트 케이스마다 I가 필요한 양보다 더 많은 운동을 하고 있다면 -1을 출력하고, 아니라면 추가로 몇 분을 더 운동해야 하는지 출력한다.

X-L<0 : result = L-X
X-L>=0 :
    U-L>=0 : result = 0
    U-L <0 : result = -1
'''

T = int(input())
for tc in range(1, T+1):
    L, U, X = map(int, input().split())

    if X - L < 0:
        result = L - X
    elif X - L >= 0:
        if U - X > 0:
            result = 0
        else:
            result = -1

    print(f'#{tc} {result}')