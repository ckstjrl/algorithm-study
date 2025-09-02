# 2346. 풍선 터뜨리기

N = int(input())    # 풍선의 수 (1~N)
nums = list(map(int, input().split()))  # 각 풍선에 있는 수
balloons = list(range(1, N+1))  # 풍선
pop_lst = []                    # 터진 풍선 순서대로

pos = 0     # 현재 (터뜨릴) 풍선 인덱스 
for _ in range(N):
    balloon_n = balloons.pop(pos)   # 풍선 번호
    move_n = nums.pop(pos)          # 풍선에 있는 숫자
    pop_lst.append(balloon_n)       # 터뜨리고 pop_lst에 넣기

    if not balloons:    # 다 터뜨려서 남은 풍선 없음; 종료 
        break
    
    # 다음 풍선 터뜨리기 위해 인덱스 움직이기
    # 인덱스가 balloons 배열 길이 벗어나지 않도록 조정 
    if move_n > 0:
        pos = (pos + move_n -1) % len(balloons)
    else:
        pos = (pos + move_n) % len(balloons)

print(*pop_lst)

