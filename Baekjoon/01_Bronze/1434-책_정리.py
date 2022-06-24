# 책 정리

N, M = map(int, input().split())
box = list(map(int, input().split()))
book = list(map(int, input().split()))
now_box = 0
now_book = 0

while True:
    if now_box >= N or now_book >= M:
        break
    if box[now_box] >= book[now_book]:
        box[now_box] = box[now_box] - book[now_book]
        now_book += 1
        continue
    else:
        now_box += 1
print(sum(box))