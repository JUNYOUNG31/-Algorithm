#  친구


N = int(input())
arr = []
ans = 0
visit = [[0] * N for i in range(N)]
for i in range(N):
    arr.append(list(input().strip()))


def func():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if arr[i][j] == "Y" or (arr[i][k] == "Y" and arr[k][j] == "Y"):
                    visit[i][j] = 1


func()
for i in range(N):
    cnt = 0
    for j in range(N):
        if visit[i][j] == 1:
            cnt += 1
    ans = max(ans, cnt)
print(ans)