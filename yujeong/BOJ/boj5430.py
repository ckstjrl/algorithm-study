# 5430. AC

T = int(input())
for tc in range(T):
    p = input()         # 수행할 함수
    n = int(input())    # 배열에 들어있는 수 개수
    arr = input()
    nums = arr[1:-1].split(',')

    if n == 0:              # n=0이면 별도로 초기화 필요
        nums = []
    if p.count('D') > n:    # 배열의 숫자 개수보다 D가 많으면 error
        print('error')
        continue

    reverse = False         # R이 홀수번 나올 때만 뒤집기 수행하기 위한 변수
    for cmd in p:
        if cmd == 'R':
            reverse = not reverse
        elif cmd == 'D':
            if reverse:     # 뒤집어야 하므로 제일 오른쪽 수 제거
                nums.pop()
            else:           # 아닐 때는 원래 규칙대로 왼쪽 수 제거
                nums.pop(0)
    # 출력            
    if reverse:             # R이 홀수번 나옴; 뒤집은 후 출력
        nums.reverse()
        print('[' + ','.join(nums) + ']')
    else:                   # R이 짝수번 나옴; 뒤집을 필요 없이 출력 
        print('[' + ','.join(nums) + ']')