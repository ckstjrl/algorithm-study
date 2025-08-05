# SWEA6485 : 삼성시의 버스 노선
# 삼성시에 있는 5,000개의 버스 정류장은 관리의 편의를 위해 1에서 5,000까지 번호가 붙어 있다.
# 그리고 버스 노선은 N개가 있는데, i번째 버스 노선은 번호가 Ai이상이고,
# Bi이하인 모든 정류장만을 다니는 버스 노선이다.
# P개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지 구하는 프로그램을 작성하라.

# 해결 방법 : 카운팅 배열을 사용하여 각 정류장마다 지나는 노선 수를 기록

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input()) # 버스 노선 수
    bus_route = []

    arr = [0] * 5001 # arr[i]으로 i번 정류장을 지나는 노선의 개수를 저장

    for i in range(N):
        a, b = map(int, input().split()) # 버스 노선의 시작과 끝
        for j in range(a, b+1): # 해당 노선의 모든 정류장에 카운트 +1
            arr[j] += 1

    P = int(input()) # P개의 정류장에 대해 노선 개수를 알고 싶음

    new_arr = []
    for i in range(P):
        new_arr.append(str(arr[int(input())]))
        # int(input()) : 정류장 번호 입력받음
        # arr[~] : 입력받은 정류장의 노선 개수 arr 배열에서 조회
    
    result = ''.join(new_arr)
    print(f'#{test_case} {result}')

    








