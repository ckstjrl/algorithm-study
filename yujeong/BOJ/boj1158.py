# 1158. 요세푸스 문제

N, K = map(int, input().split())

lst = list(range(1, N+1))   # 1부터 N까지 사람들
newlst = [] # 꺼내지는 사람들을 담을 리스트

i = 0   # 출발할 인덱스 
for k in range(N):  # 사람이 모두 꺼내지려면 N번 꺼내야 함
    i += K-1    # K번째 사람
    i %= (N-k)  # 인덱스가 리스트 범위 넘어설 경우 방지 
    newlst.append(str(lst.pop(i)))  # 꺼내서 newlst에 담기

# 형식에 맞게 출력
print('<' + ', '.join(newlst) + '>')