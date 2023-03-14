# 후보 추천하기

N = int(input())
num = int(input())
student = list(map(int, input().split()))
arr = []
vote = []

for i in range(num):
    if student[i] in arr:
        for j in range(len(arr)):
            if student[i] == arr[j]:
                vote[j] += 1
    else:
        if len(arr) >= N:
            for j in range(N):
                if vote[j] == min(vote):
                    del arr[j]
                    del vote[j]
                    break
        arr.append(student[i])
        vote.append(1)

arr.sort()
print(*arr)