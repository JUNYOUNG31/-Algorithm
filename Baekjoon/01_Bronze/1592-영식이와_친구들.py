# 영식이와 친구들

N, M, L = map(int, input().split())

people = [0]*N
ans = 0
i = 0
while True:
    people[i] += 1
    if people[i] == M:
        print(ans)
        break
    elif people[i] % 2 == 1:
        i = (i+L) % N
    else:
        i = (i+(N-L)) % N
    ans += 1