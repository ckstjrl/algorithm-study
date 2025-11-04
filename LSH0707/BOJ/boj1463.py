N = int(input())
q = []
visited = set()  # 만들었던 숫자
q.append([N, 0])  # [현재숫자, 시행횟수] 큐에 추가
while q:
        p = q.pop(0)  # bfs
        a = p[0]  # 현재숫자
        b = p[1]  # 시행횟수
        if a == 1:  # 1에 도달한 경우 시행횟수 출력하고 break
            print(b)
            break
        if a not in visited:  # 만들어본적없는 숫자인 경우 만든숫자 세트에 추가하고 [다음숫자, 시행회수+1] 큐에추가
            visited.add(a) 
            if a % 3 == 0:  
                q.append([a//3, b+1])
            if a % 2 == 0:
                q.append([a//2, b+1])
            q.append([a-1, b+1])
