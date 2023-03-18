# 금민수의 개수

A, B = map(int, input().split())
q = [4, 7]
ans = 0
while len(q) > 1:
    temp = q[0]
    q.pop(0)
    if temp <= B:
        if A <= temp:
            ans += 1
        q.append(temp*10 + 4)
        q.append(temp*10 + 7)

print(ans)