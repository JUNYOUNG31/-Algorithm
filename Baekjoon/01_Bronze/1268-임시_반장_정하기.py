# 임시 반장 정하기

num = int(input())
cls = []
visited = [0] * num
for i in range(num):
    cls.append(list(map(int, input().split())))
    visited[i] = [0] * num

for i in range(5):
    for j in range(num):
        for k in range(j + 1, num):
            if cls[j][i] == cls[k][i]:
                visited[k][j] = 1
                visited[j][k] = 1
cnt = []
for i in visited:
    cnt.append(i.count(1))
# print(visited)
# print(cnt)
print(cnt.index(max(cnt)) + 1)

