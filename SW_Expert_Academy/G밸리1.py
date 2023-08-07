# 알고리즘 1문제

# 읽고 말하는 대로 다음 항을 도출하는 수열이다. 보고 말하기 수열이라고도 하며,프랑스의
# 유명소설가 베르나르 베르베르의 소설<개미>에 등장하여 한국에서는 개미 수열이라고도 불린다.


n = int(input())
arr = [1, 2, 1, 1]


for i in range(3, n-1):
    cnt = 1
    num = len(arr)
    # print(num)
    temp = []
    for j in range(1, num):
        if arr[j] != arr[j-1]:
            temp.append(cnt)
            temp.append(arr[j-1])
            cnt = 1
            if j == num-1:
                temp.append(cnt)
                temp.append(arr[j])
        else:
            cnt += 1
            if j == num-1:
                temp.append(cnt)
                temp.append(arr[j])

    arr = temp

print(arr)
ans = len(arr)//2
temp = [str(arr[ans-1]), str(arr[ans])]
t = ''.join(temp)
print(t)