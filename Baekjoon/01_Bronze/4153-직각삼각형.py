# 직각삼각형

# 과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각 삼각형인것을 알아냈다.
# 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.

while True:
        arr = list(map(int, input().split()))
        max_num = max(arr)
        if sum(arr) == 0:
                break
        arr.remove(max_num)
        if arr[0]**2 + arr[1]**2 == max_num**2:
                print('right')
        else:
                print('wrong')