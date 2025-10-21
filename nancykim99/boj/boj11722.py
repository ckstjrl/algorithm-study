'''
BOJ11722 / D2): 가장 긴 감소하는 부분 수열

해결 방법 : 
1. 처음에는 i를 기준으로 뒷 번호를 확인하는 방식으로 체크하려고 했는데, 함수를 만들다가 Recursion Error가 나서 포기.
'''
# def longest_sequence(i, j, len_seq):
#     global max_len
#     if i == (N-1):
#         return
#     if j == (N-1):
#         if max_len < len_seq:
#             max_len = len_seq
#         longest_sequence(i+1, i+2, 0)
#     if j < N and arr[i] >= arr[j]:
#         longest_sequence(i, j+1, len_seq)
#     else:
#         longest_sequence(i, j+1, len_seq+1)
'''
2. i를 기준으로 앞 번호를 확인하는 방식으로 체크.
    1) 인덱스 1부터 N까지 순회하면서 -> i
    2) i 앞의 숫자들을 순회하면서 -> j
    3) 앞 숫자가 i보다 클 경우
    4-1) 앞 숫자 중 이미 큰 순열이 만들어진 경우, 앞 숫자 + 1
    4-2) 이미 순열이 더 큰 경우, 유지

* 그래도 DP 중엔 금방 해결 방법을 찾은 편인듯 싶다. 배열에서 뒷 숫자만 비교할 생각이었는데, 앞 숫자를 비교하는 방법도 생각해놔야 할듯.
'''

N = int(input())
arr = list(map(int, input().split()))

check_max_seq = [1] * N # 숫자 하나만 있어도 순열이기 때문에 1로 이뤄진 배열

for i in range(1, N): # 인덱스 0을 제외한 나머지 숫자 순회
    for j in range(i): # i보다 앞 숫자들 순회하면서
        if arr[j] > arr[i]: # j가 i보다 크면,
            check_max_seq[i] = max(check_max_seq[i], check_max_seq[j]+1)

print(max(check_max_seq))