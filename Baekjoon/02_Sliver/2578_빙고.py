# 빙고
bingo = [list(map(int, input().split())) for _ in range(5)]     # 빙고 판 입력

line = 0                                                        # 빙고 라인 수
cnt = 0                                                         # 사회자가 부르는 횟수
visited = [[0] * 5 for _ in range(5)]                           # 방문 기록
calls = [list(map(int, input().split())) for _ in range(5)]     # 부르는 번호
for r in range(5):                                              # 부르는 번호의 위치를 찾기 위한 r
    for c in range(5):                                          # c
        for i in range(5):                                      # 빙고에서 그값을 찾기 위한 r => i
            for j in range(5):                                  # c => j
                if calls[r][c] == bingo[i][j]:                  # 두값이 같으면
                    visited[i][j] = 1                           # 방문 체크
                    cnt += 1                                    # 부른 횟수 체크
                    line = 0                                    # 라인은 아직 0 줄
                    if visited[0][0] == 1 and visited[1][1] == 1 and visited[2][2] == 1 and visited[3][3] == 1 and visited[4][4] == 1:
                        line += 1                               # \ 대각선에 해당하는 부분
                    if visited[4][0] == 1 and visited[3][1] == 1 and visited[2][2] == 1 and visited[1][3] == 1 and visited[0][4] == 1:
                        line += 1                               # / 대각선에 해당하는 부분
                    for row in range(5):                        # 가로로 빙고일 경우
                        if sum(visited[row]) == 5:              # 각 자리의 합을 다더해서 5이면 1,1,1,1,1 인 경우
                            line += 1                           # 라인 추가
                    for col in range(5):                        # 세로로 빙고일 경우
                        num = 0                                 # num 변수
                        for rows in range(5):                   # 세로 값 반복
                            if visited[rows][col] == 1:         # 세로줄로 값이 1이라면
                                num += 1                        # num 에 1 추가
                        if num == 5:                            # 다돌려서 num 이 5면
                            line += 1                           # 라인 추가
                    if line >= 3:                               # 라인이 3을 넘기면
                        break                                   # 스톱
                if line >= 3:                                   # 스톱
                    break
            if line >= 3:                                       # 스톱
                break
        if line >= 3:                                           # 스톱
            break
    if line >= 3:                                               # 스톱
        print(cnt)                                              # 카운트 출력
        break