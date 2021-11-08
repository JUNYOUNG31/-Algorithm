# 카펫

# Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로
# 칠해져 있는 격자 모양 카펫을 봤습니다. Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의
# 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.
# Leo가 본 카펫에서 갈색 격자의 수 brown, # 노란색 격자의 수 yellow가 매개변수로 주어질 때
# 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.


def solution(brown, yellow):
    answer = []
    yellow_s = []                       # 노란색의 약수
    for i in range(1, yellow+1):        # 노란색까지 돌아서
        if yellow % i == 0:             # 약수찾으면
            yellow_s.append(i)          # 추가
    print(yellow_s)
    for i in range(len(yellow_s)):      # 약수의 개수만큼돌아서
        y = yellow_s[i]                 # 세로
        x = yellow//y                    # 가로
        if 2*(x+2) + 2*y == brown:      # (x+2) * 2 (상하) + 2*y (좌우) = 갈색 수
            answer = [x+2, y+2]    # 정답은 가로 세로
            return answer


# brown = 10
# brown = 8
brown = 24
# yellow = 2
# yellow = 1
yellow = 24

print(solution(brown,yellow))