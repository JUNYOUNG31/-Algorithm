# 등수 구하기

N, score, P = map(int, input().split())
if N:
    rank = list(map(int, input().split()))
    rank.append(score)
    rank.sort(reverse=True)
    # print(rank)
    ans = rank.index(score) + 1
    if ans > P:
        print(-1)
    else:
        if N == P and score == rank[-1]:
            print(-1)
        else:
            print(ans)
else:
    print(1)