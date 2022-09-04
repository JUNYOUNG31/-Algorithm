# 숙제
import heapq

T = int(input())
for tc in range(T):
    n, S = map(int, input().split())
    time = list(map(int, input().split()))
    score = list(map(int, input().split()))
    arr = []
    ans = 0
    hq = []
    for j in range(n):
        arr.append((score[j], time[j]))
    arr = sorted(arr, key=lambda x: x[1])

    for i in range(n):                                  # 문제를 탐색
        if arr[i][1] <= S:                              # 현재시간보다 문제가 빠르게 나오면
            heapq.heappush(hq, (-arr[i][0], arr[i]))    # 일단 저장한다 벌점 점수가 높은 순으로
        else:                                           # 현재시간보다 크면
            s = S
            while hq:                                   # 비었는지 확인하고
                if s == arr[i][1]:                      # 근데 시간이 지나다보니 지금 문제랑 같다면 멈추고
                    break
                temp = heapq.heappop(hq)                # 맨앞에 있는게 제일 벌점이 높으니깐 빼서
                ans += temp[1][0]*(s-temp[1][1])        # 점수를 더하고
                s += 1            # 시간 늘리고
            heapq.heappush(hq, (-arr[i][0], arr[i]))    # 그문제를 넣어준다 hq에
            S = arr[i][1]

    while hq:                                           # 비었는지 확인하고
        temp = heapq.heappop(hq)                        # 맨앞에 있는게 제일 벌점이 높으니깐 빼서
        ans += temp[1][0] * (S - temp[1][1])            # 점수를 더하고
        S += 1                                          # 시간 늘리고
    print(ans)