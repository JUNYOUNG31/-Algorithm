# 아이폰 9S

N = int(input())
B = []
for i in range(N):
    temp = int(input())
    B.append(temp)

check = set(B)
max_cnt = 1
for b in B:
    cnt = 1
    same = -1
    for i in B:
        if i != b:
            if same == -1:
                same = i
            else:
                if same == i:
                    cnt += 1
                else:
                    max_cnt = max(max_cnt, cnt)
                    same = i
                    cnt = 1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)