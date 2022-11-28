# 3번 문제


def solution(s, times):
    answer = [1, 0]
    year, month, day, hour, minute, second = list(map(int, s.split(":")))
    arr = [year, month, day]
    flag = 1
    # print(year, month, day, hour, minute, second)
    for i in times:
        check_day = day
        d, h, m, s = map(int, i.split(":"))
        second += s
        if second >= 60:
            temp_s = second // 60
            minute += temp_s
            second %= 60
        minute += m
        if minute >= 60:
            temp_m = minute // 60
            hour += temp_m
            minute %= 60
        hour += h
        if hour >= 24:
            temp_h = hour // 24
            day += temp_h
            hour %= 24
        day += d
        if day >= 30:
            temp_d = day // 30
            month += temp_d
            day %= 30
        if month >= 12:
            temp_M = month // 12
            year += temp_M
            month %= 12

        if check_day == day or check_day + 1 == day:
            flag = 1
        else:
            flag = 0
            answer[0] = 0
        # print(year, month, day, hour, minute, second)
    # 총 저축기간
    num1 = year - arr[0]
    if num1 > 0:
        answer[1] += 360 * num1
    num2 = month - arr[1]
    if num2 > 0:
        answer[1] += 30 * num2
    num3 = day - arr[2] + 1
    answer[1] += num3

    return answer




# s = "2021:04:12:16:08:35"
# times = ["01:06:30:00", "01:04:12:00"]

s = "2021:04:12:16:08:35"
# ["01:06:30:00", "00:01:12:00"]
times = ["01:06:30:00", "00:01:12:00", "20:01:12:00"]
#
# "2021:04:12:16:10:42"
# ["01:06:30:00"]
#
# "2021:04:12:16:08:35"
# ["01:06:30:00", "01:01:12:00", "00:00:09:25"]


print(solution(s, times))


# [0, 4]
# [1, 2]
# [1, 2]
# [1, 4]