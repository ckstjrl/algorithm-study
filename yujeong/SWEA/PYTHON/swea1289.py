# 1289. 원재의 메모리 복구하기 / D3

# 초기값(모든 bit 0) 에서 주어진 값으로 돌아가는데 필요한 수정 횟수.

T = int(input())

for t in range(T):
    org_mm = list(map(int, input()))
    cnt = 0

    cur_num = False # bit 0 <-> 1 전환을 위해 boolean으로
    for i in org_mm: # 원래 상태 메모리 숫자를 앞에서부터 탐색하며
        if i != cur_num: # 덮어씌우고 있는 숫자와 다르면 새로운 숫자로 덮어씌워야 함 
            cnt += 1
            cur_num = not cur_num # 0 <-> 1

    print(f'#{t+1} {cnt}')