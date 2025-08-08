# 원재의 메모리 복구하기 / D3
T = int(input())
for tc in range(1, T+1):
    bits = list(map(int, input())) # bits 리스트로 받기
    
    a = bits.index(1) # 첫번째 1이 되는 인덱스를 찾아 a에 할당
    
    cnt = 1 # 첫번째 1이 입력된 상태로 생각하기 때문에 초기값 1로 설정
    for i in range(a+1, len(bits)): # index a부터 차례대로 비교하는데
        if bits[i-1] != bits[i]: # 비교식을 이렇게 작성하여 range 범위를 a+1로 설정하고
            cnt += 1             # 숫자가 달라질때마다 cnt 1씩 증가
    print(f'#{tc} {cnt}')