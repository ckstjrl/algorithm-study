#BOJ10798 세로읽기

arr = list(input() for _ in range(5))

ans = ''

# 한줄에 주어질수 있는 최대 단어의 길이
for i in range(15):
    # 5줄에 걸쳐서 문자열이 주어짐
    for j in range(5):
        # 이 부분에 대해서 다른 분의 코드를 참고하였는데 위에서 받은 각 줄의 길이를 기반으로 out of index를 방지하여 주었다
        # 유의: list 안에 list개념을 잊지 말자 (여전히 리스트의 길이를 이용할 수 있다)
        if i <= len(arr[j])-1:
            ans += arr[j][i]

print(ans)