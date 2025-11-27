t = int(input())
for test_case in range(1, t + 1):
    h, w = map(int, input().split())
    field = []
    for _ in range(h):
        field.append(list(input()))

    n = int(input())
    commands = input()
    
    # 초기 상태 파악
    for i in range(h):
        for j in range(w):
            if field[i][j] in ["^", "v", "<", ">"]:
                current_i = i
                current_j = j
                dir = field[i][j]

    # 이동 설정
    di = {"U":-1, "D":1, "L":0, "R":0}
    dj = {"U":0, "D":0, "L":-1, "R":1}
    c = {"U":"^", "D":"v", "L":"<", "R":">"}

    # 커맨드 처리
    for command in commands:
        if command != "S":
            next_i = current_i+di[command]
            next_j = current_j+dj[command]
            dir = c[command]

            if 0 <= next_i < h and 0 <= next_j < w:
                if field[next_i][next_j] == ".":
                    field[current_i][current_j] = "."
                    field[next_i][next_j] = dir
                    current_i = next_i
                    current_j = next_j
                else:
                    field[current_i][current_j] = dir
            else:
                field[current_i][current_j] = dir
        else:
            for each in c:
                if c[each] == dir:
                    shoot_command = each

            shoot_i = current_i
            shoot_j = current_j
            
            while True:
                shoot_next_i = shoot_i+di[shoot_command]
                shoot_next_j = shoot_j+dj[shoot_command]
                if not (0 <= shoot_next_i < h and 0 <= shoot_next_j < w):
                    break
                if field[shoot_next_i][shoot_next_j] == "#":
                    break
                elif field[shoot_next_i][shoot_next_j] == "*":
                    field[shoot_next_i][shoot_next_j] = "."
                    break
                else:
                    shoot_i = shoot_next_i
                    shoot_j = shoot_next_j

    print(f"#{test_case}", end=" ")
    for i in field:
        print("".join(i))