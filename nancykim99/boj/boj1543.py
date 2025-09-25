'''
BOJ1543 / D2): 문서 검색

해결 방법 : 브루트포스 알고리즘. 브루트포스 알고리즘이 바로 떠오르지 않는다. 문자열 관련 문제를 더 풀어봐야할 듯.
'''

base = input()
search = input()

cnt = 0
idx = 0
while idx <= len(base) - len(search): # 인덱스가 base를 벗어나지 않고, 마지막 len(search)만큼 비교할 수 있을 만큼
    if base[idx : idx + len(search)] == search: # 인덱스부터 단어 길이 만큼 단어랑 같은지 비교
        cnt += 1 # 같으면 cnt + 1
        idx += len(search) # 단어 길이만큼 idx 추가해서 idx 뛰어넘기
    else: # 단어를 못 찾은 경우
        idx += 1 # 인덱스 + 1 해서 다시 찾기

print(cnt)