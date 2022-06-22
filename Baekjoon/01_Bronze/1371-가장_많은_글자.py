# 가장 많은 글자

import sys
arr = [0]*26
s = sys.stdin.read().replace('\n', '').replace(' ','')
for i in s:
    arr[ord(i)-97] += 1
for j in range(26):
    if arr[j] == max(arr):
        print(chr(97+j), end ='')