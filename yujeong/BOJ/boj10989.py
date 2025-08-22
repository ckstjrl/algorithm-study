# 10989. 수 정렬하기 3

import sys
input = sys.stdin.readline

# 메모리 제한이 빡세기 때문에 append -> sort를 사용하기 쉽지 않다.
# 각 숫자는 10000보다 작거나 같다는 점을 고려해, 카운팅 정렬을 활용하자!!
cnt = [0] * 10001
N = int(input())
for _ in range(N):
    num = int(input())      # 입력받는 숫자: num
    cnt[num] += 1           # num이 등장한 횟수 +1

for i in range(1, 10001):
    if cnt[i]:              # 그 숫자가 등장했으면
        for _ in range(cnt[i]):
            print(i)        # 등장한 횟수만큼 한 줄에 하나씩 출력