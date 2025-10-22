# BOJ 2812. 크게 만들기 / D3
'''
문제
N자리 숫자가 주어졌을 때, 여기서 숫자 K개를 지워서 얻을 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 주어진다. (1 ≤ K < N ≤ 500,000)

둘째 줄에 N자리 숫자가 주어진다. 이 수는 0으로 시작하지 않는다.

출력
입력으로 주어진 숫자에서 K개를 지웠을 때 얻을 수 있는 가장 큰 수를 출력한다.
'''
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
num = list(map(int, input().strip()))

best = []
start_idx = 0
remove_n = K
need = N-K
while need > 0:
    end_idx = start_idx + remove_n
    if end_idx >= N:
        end_idx = N-1
    max_s = 0
    max_idx = start_idx
    for i in range(start_idx, end_idx+1):
        if num[i] > max_s:
            max_s = num[i]
            max_idx = i # max_idx가 다음 숫자 -> 앞 숫자들은 다 지워지는 것 -> 지워야하는 숫자 개수는 max_idx-start_idx
            if max_s == 9:
                break

    best.append(max_s)
    remove_n -= (max_idx - start_idx)

    start_idx = max_idx + 1
    need -= 1

print(''.join(map(str, best)))

'''
앞에서부터 지워야하는 숫자 개수만큼 뽑아서 그중 제일 큰 숫자를 맨앞자리로 넣고
그 다음 순서부터는 아까 뽑은 제일 큰 숫자 다음 인덱스부터 지워야하는 숫자 개수 만큼 뽑아서 다음 자리로 넣고
반복진행
여기서 지워야하는 숫자는 뽑은 숫자들 중 제일 큰 숫자 앞에 있는 숫자 개수만큼 빼줌

예시로
10 4
4177252841
를 진행하면
step1
- 4, 1, 7, 7, 2 중 가장 큰 숫자 7이므로 best 리스트에 7을 넣음,
- 그러면 7 앞에 있는 4, 1이 지워짐. 지워야하는 수는 4 - 2 = 2 
step2
- 인덱스 3부터 다시 확인
- 7, 2, 5 중 가장 큰 수 7이므로 best에 7 넣음
- 지우는 숫자 없음
step3
- 인덱스 4부터 다시 확인
- 2, 5, 2 중 가장 큰 수 5이므로 best에 5넣음
- 5 앞에 있는 2 지워짐, 지워야하는 수는 2 - 1
step4
-인덱스 6부터 다시 확인
- 2, 8 중 가장 큰 수 8이므로 best에 8 넣음
- 8 앞에 있는 2 지워짐, 지워야하는 수 1 - 1 = 0

while 조건은 필요한 숫자 > 0 인 경우 인데 결국 이 경우는 지워야하는 수 == 0 이 되면 끝까지 best에 넣는 것만 진행한다는 의미
best = [7, 7, 5, 8, 4, 1]이 된다.
'''
'''
시간 복잡도 때문에 안될 줄 알았는데 생각보다 테스트케이스가 여유로워서 통과한듯하다.
'''