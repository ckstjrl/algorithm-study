# BOJ 5052. 전화번호 목록 (D3 / G4)
import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    N = int(input())
    
    # 셋으로 저장하고 완탐 갈기기
    phone_set = set()
    for _ in range(N):
        phone_set.add(input())
    
    is_ok = True
    
    
    for phone in phone_set:
        #한 넘버의 모든 경우의 수가 다른 넘버중에 있는지
        for i in range(1, len(phone)):
            prefix = phone[:i]
            
            # 있으면 False 종료
            if prefix in phone_set:
                is_ok = False
                break
        if not is_ok:
            break
    
    if is_ok:
        print("YES")
    else:
        print("NO")