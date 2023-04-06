# 2048

# 5번 이동해서 얻을수 있는 가장 큰 수
# 상 하 좌 우 움직여서 가장 큰수
# 또 그걸 상 하 좌 우  큰수
# 5번 반복?

import copy

N = int(input())
pan = []
for i in range(N):
    temp = list(map(int, input().split()))
    pan.append(temp)
# for i in range(N):
#     print(pan[i])

# 상
def up(pan):
    for i in range(N):
        up_idx = 0             # 인데스
        for j in range(N):
            # 위에랑 비교해서
            # 같으면 2배
            # 다르면 그대로
            # 0 이면 옮기기
            if pan[j][i] != 0:                  # 현재 판이 0 이 아니면
                now = pan[j][i]                 # 현재값을 저장
                pan[j][i] = 0                   # 현재 판을 0 으로 변경
                if pan[up_idx][i] == now:       # 위의 판이 현재값과 같다면
                    pan[up_idx][i] = 2 * now    # 위의 판을 2배 하고
                    up_idx += 1                 # 현재 인덱스를 1 늘려서 다음 줄로 변경
                elif pan[up_idx][i] == 0:       # 위의 판이 0 이라면
                    pan[up_idx][i] = now        # 위의 판을 현재 값으로 변경
                else:                           # 위의 판이랑 다르면
                    up_idx += 1                 # 인덱스를 1 늘리고
                    pan[up_idx][i] = now        # 다음 판으로 변경
    return pan

# arr1 = up(pan)
# for i in range(3):
#     print(arr1[i])
# 하
def down(pan):
    for i in range(N):
        down_idx = N-1             # 인데스
        for j in range(N-1,-1,-1):
            # 밑이랑 비교해서
            # 같으면 2배
            # 다르면 그대로
            # 0 이면 옮기기
            if pan[j][i] != 0:
                now = pan[j][i]
                pan[j][i] = 0
                if pan[down_idx][i] == now:
                    pan[down_idx][i] = 2 * now
                    down_idx -= 1
                elif pan[down_idx][i] == 0:
                    pan[down_idx][i] = now
                else:
                    down_idx -= 1
                    pan[down_idx][i] = now
    return pan


# arr2 = down(pan)
# for i in range(3):
#     print(arr2[i])
# 좌

def left(pan):
    for i in range(N):
        left_idx = 0             # 인데스
        for j in range(N):
            # 왼쪽에랑 비교해서
            # 같으면 2배
            # 다르면 그대로
            # 0 이면 옮기기
            if pan[i][j] != 0:
                now = pan[i][j]
                pan[i][j] = 0
                if pan[i][left_idx] == now:
                    pan[i][left_idx] = 2 * now
                    left_idx += 1
                elif pan[i][left_idx] == 0:
                    pan[i][left_idx] = now
                else:
                    left_idx += 1
                    pan[i][left_idx] = now
    return pan

# arr3 = left(pan)
# for i in range(3):
#     print(arr3[i])
# 우
def right(pan):
    for i in range(N):
        right_idx = N-1             # 인데스
        for j in range(N-1,-1,-1):
            # 왼쪽에랑 비교해서
            # 같으면 2배
            # 다르면 그대로
            # 0 이면 옮기기
            if pan[i][j] != 0:
                now = pan[i][j]
                pan[i][j] = 0
                if pan[i][right_idx] == now:
                    pan[i][right_idx] = 2 * now
                    right_idx -= 1
                elif pan[i][right_idx] == 0:
                    pan[i][right_idx] = now
                else:
                    right_idx -= 1
                    pan[i][right_idx] = now
    return pan

# arr4 = right(pan)
# for i in range(3):
#     print(arr4[i])

ans = 0


def dfs(pan, cnt):
    global ans
    if cnt == 5:
        for i in range(N):
            ans = max(ans, max(pan[i]))
        return
    dfs(up(copy.deepcopy(pan)), cnt+1)
    dfs(down(copy.deepcopy(pan)), cnt+1)
    dfs(left(copy.deepcopy(pan)), cnt+1)
    dfs(right(copy.deepcopy(pan)), cnt+1)


dfs(pan, 0)
print(ans)