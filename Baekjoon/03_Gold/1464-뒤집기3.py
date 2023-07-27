# 뒤집기 3

arr = list(input())
ans = []


def sort_temp(slice_arr, next_arr):
    temp1 = ''.join(slice_arr+[next_arr])
    temp2 = ''.join(slice_arr[::-1] + [next_arr])
    temp1_re = ''.join((slice_arr+[next_arr])[::-1])
    temp2_re = ''.join((slice_arr[::-1] + [next_arr])[::-1])
    temp = [temp1, temp2, temp1_re, temp2_re]
    temp.sort()
    print(temp)
    return temp[0]


for i in range(1, len(arr)):
    temp = sort_temp(arr[:i], arr[i])
    temp = list(temp)
    arr = temp + arr[i+1:]

ans = ''.join(arr)
print(ans)