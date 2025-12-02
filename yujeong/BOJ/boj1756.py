# 1756. 피자 굽기

import sys
input = sys.stdin.readline

D, N = map(int, input().split())    # 오븐 깊이 D, 피자 반죽 N개

deep = list(map(int, input().split()))  # 층별 오븐 지름
pizza = list(map(int, input().split())) # 피자 반죽 지름 

'''
오븐 구조 재정리
아래층 지름이 위층 지름보다 커도 어차피 더 작은 만큼(=위층 지름) 만큼만 쓸 수 있음
'''
oven = [deep[0]]
for d in range(1, D):
    if deep[d] > oven[d-1]:
        oven.append(oven[d-1])
    else:
        oven.append(deep[d])

'''
피자 반죽 넣기
'''
idx = 0     # 피자 반죽 인덱스
top = D     # 마지막 피자 반죽 위치(깊이)

for r in range(D-1, -1, -1):    # 아래에서부터 피자 올리기
    if idx >= N:    # 모든 피자 반죽 다 넣음; 종료
        break
    if oven[r] >= pizza[idx]:   # 이 층에 idx번 피자 반죽 넣을 수 있음
        idx += 1                # 이제 다음 피자 반죽 보기
        top = min(top, r+1)     # 마지막 피자 반죽 위치 갱신

# 모든 피자가 다 오븐에 들어갔으면 top, 아니면 0 출력 
print(top if idx==N else 0) 

