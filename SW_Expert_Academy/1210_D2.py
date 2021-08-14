# Ladder1
dr = [0, 0, -1]  # 우 좌 상
dc = [1, -1, 0]

for tc in range(1, 11):
    T = int(input())
    Ladder = [list(map(int, input().split())) for _ in range(100)]
    d = 0
    r = 0
    c = 0
    ans_i = 0                      # 출발 지점
    for i in range(100):           # 100 번 반복하는데  거꾸로 시작
        if Ladder[99][i] == 2:     # 마지막행  i 번째가 2 이라면
            r = 99                 # 행좌표 99
            c = i                  # 열좌표
            now = 0                # 현재 상태
    while r != 0:                  # 행이 100이 될때까지 반복
        if 0 <= r+dr[0] < 100 and 0 <= c+dc[0] < 100:        # 오른쪽으로 움직일때 벽을 만나지 않으면서
            if Ladder[r+dr[0]][c+dc[0]] == 1 and now != 1:   # 오른쪽옆이 1이고 현재상태가 1(왼쪽으로움직이는게 아닐때)
                r, c = r+dr[0], c+dc[0]                      # 그방향으로 진행하고
                now = 2                                      # 현재상태 2
                continue
        if 0 <= r+dr[1] < 100 and 0 <= c+dc[1] < 100:        # 왼쪽으로 움직일때 벽을 만나지 않으면서
            if Ladder[r+dr[1]][c+dc[1]] == 1 and now != 2:   # 왼쪽옆이 1이고 현재상태가 2(오른쪽으로 움직이는게 아닐때)
                r, c = r+dr[1], c+dc[1]                      # 그방향으로 진행하고
                now = 1                                      # 현재상태 1
                continue
        r, c = r + dr[2], c + dc[2]                          # 둘다 아니면 위로 한칸
        now = 0                                              # 현재상태 0

    ans_i = c                                                # 현재출발 지점
    print("#{} {}".format(tc, ans_i))


    #######
    # ladder
    def search(start):  # 도착지까지 위로 올라가는 함수
        i = 99  # 행
        j = start  # 열
        while i > 0:  # 맨 윗줄에 도착하기 전까지 위로 올라감
            i -= 1  # 위로 한 칸 이동
            if j > 0 and ladder[i][j - 1] == 1:  # 왼쪽칸이 있고 1이면
                while j > 0 and ladder[i][j - 1] == 1:  # 사다리를 벗어나거나 0일때까지
                    j -= 1  # 왼쪽이동
            elif j < 99 and ladder[i][j + 1] == 1:  # 오른쪽칸이 있고 1이면
                while j < 99 and ladder[i][j + 1] == 1:
                    j += 1
                    # 좌우가 0이면 위로
        return j  # 0번 행에 도착했을때의 열(출발지)


    T = 10
    for tc in range(1, T + 1):
        n = int(input())
        ladder = [list(map(int, input().split())) for _ in range(100)]
        # 도착지 검색
        goal = 0
        for i in range(100):
            if ladder[99][i] == 2:
                goal = i
        ans = search(goal)
        print("#{} {}".format(tc, ans))