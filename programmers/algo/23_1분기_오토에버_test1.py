# 데이터의 key 와 value가 주어질때  1번 리스트와 2번 리스트를 비교했을때 데이터의 생성 삭제 변경
# 된것의 숫자와 key 값

N = int(input())


arr1 = {}
arr2 = {}
for i in range(N):
    k, v = list(input().split())
    arr1[k] = v

M = int(input())
for i in range(M):
    k, v = list(input().split())
    arr2[k] = v


def Add():
    temp = []
    for i in arr2:
        if not i in arr1:
            temp.append(i)
    temp.sort()
    return temp


def Delete():
    temp = []
    for i in arr1:
        if not i in arr2:
            temp.append(i)
    temp.sort()
    return temp


def Change():
    temp = []
    for i in arr1:
        if i in arr2 and arr1[i] != arr2[i]:
            temp.append(i)
    temp.sort()
    return temp


add_list = Add()
delete_list = Delete()
change_list = Change()

print(len(add_list), *add_list)
print(len(delete_list), *delete_list)
print(len(change_list), *change_list)