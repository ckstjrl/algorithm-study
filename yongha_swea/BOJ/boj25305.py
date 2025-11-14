#BOJ25305 커트라인

#응시자 N, 수상자 k
N, k = map(int, input().split())

arr = list(map(int, input().split()))

#arr에서 수상자 수만큼 반복하여 최고 점수를 뽑아내기
for i in range(k):
    win = arr.pop(arr.index(max(arr)))

print(win)