# N개의 0과 1로 이루어진 수열에서 연속한 1의 개수 중 최대값을 출력하는 프로그램

T = int(input()) # 테스트 케이스

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input()))

    max_c_list = [] # 연달아서 나오는 숫자의 리스트
    c = 0 # 연달아서 나오는 숫자의 수
    c_num = 0 # 연달아서 나오는 숫자의 수의 수

    for i in range(N):
        if arr[i] == 1: # 1인 경우
            c += 1
            max_c_list += [c] # 지금까지의 c를 리스트에 추가
            c_num += 1  # 몇 번 연달아서 진행했는지 추가
        elif arr[i] == 0: # 0인 경우
            if arr[i] != arr[i-1]:
                max_c_list += [c] # 지금까지의 c를 리스트에 추가
                c_num += 1 # 몇 번 연달아서 진행했는지 추가
                c = 0 # 다시 0으로 진행

    max_c = max_c_list[0]
    for i in range(c_num): # max_c_list에서 최대값 구하기
        if max_c < max_c_list[i]:
            max_c = max_c_list[i]

    print(f'#{tc}', max_c)