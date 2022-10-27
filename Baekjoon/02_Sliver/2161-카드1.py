# 카드1

N = int(input())
card = [i for i in range(1, N+1)]
arr = []

while len(card) != 1:
    arr.append(card.pop(0))
    card.append(card.pop(0))

print(*arr ,end= " ")
print(card[0])