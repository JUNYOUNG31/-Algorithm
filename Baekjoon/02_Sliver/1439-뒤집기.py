# 뒤집기

S = input()
cnt1 = 0
cnt2 = 0

if S[0] == '0':
    cnt2 += 1
else:
    cnt1 += 1

for i in range(len(S)-1):
    if S[i] != S[i+1]:
        if S[i+1] == '1':
            cnt1 += 1
        else:
            cnt2 += 1

print(min(cnt1, cnt2))