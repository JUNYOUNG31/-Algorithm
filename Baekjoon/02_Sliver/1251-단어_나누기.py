# 단어 나누기

str = list(input())
ans = []
arr = []

for i in range(1, len(str)-1):
    for j in range(i+1, len(str)):
        x = str[:i]
        y = str[i:j]
        z = str[j:]
        x.reverse()
        y.reverse()
        z.reverse()
        arr.append(x+y+z)

for i in arr:
    ans.append(''.join(i))

answer = sorted(ans)[0]

print(answer)