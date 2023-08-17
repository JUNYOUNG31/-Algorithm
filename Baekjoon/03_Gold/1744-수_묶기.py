# 수 묶기

N = int(input())
arr_plus = []
arr_minus = []
hap = 0
for i in range(N):
    temp = int(input())
    if temp > 1:
        arr_plus.append(temp)
    elif temp <= 0:
        arr_minus.append(temp)
    else:
       hap += temp

arr_plus.sort(reverse=True)
arr_minus.sort()


if len(arr_plus) % 2 == 0:
    for i in range(0, len(arr_plus), 2):
        hap += arr_plus[i] * arr_plus[i+1]
else:
    for i in range(0, len(arr_plus)-1, 2):
        hap += arr_plus[i] * arr_plus[i+1]
    hap += arr_plus[-1]

if len(arr_minus) % 2 == 0:
    for i in range(0, len(arr_minus), 2):
        hap += arr_minus[i] * arr_minus[i+1]
else:
    for i in range(0, len(arr_minus)-1, 2):
        hap += arr_minus[i] * arr_minus[i+1]
    hap += arr_minus[-1]

print(hap)