# BOJ 1158 - 요세푸스 문제
# 0부터 N까지의 배열 리스트를 만들고, 빈 리스트가 될 때지까지 나눗셈을 뺀다 ?

N, K = map(int, input().split())
mylist = [i for i in range(1, N+1)]
ans = []
i = 0  # 현재 위치를 추적

while mylist:
    i = (i + K - 1) % len(mylist)
    # 해당 사람을 제거하고 답에 추가
    one = mylist.pop(i)
    ans.append(one)
    # i는 자동으로 다음 위치를 가리키게 됨 (pop으로 인해)

ans = str(ans).strip('[]')
print(f"<{ans}>")