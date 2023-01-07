

def solution(day1, dow1, day2):
    answer = ''
    dow = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    num = dow.index(dow1)
    if day1 < day2:
        temp = day2 - day1
        dow2 = temp % 7
        answer = dow[(num+dow2)%7]
    if day1 > day2:
        temp = day1 - day2
        dow2 = temp % 7
        answer = dow[(num-dow2)%7]
    return answer



day1 = 25
dow1 = "SUN"
day2 = 2


print(solution(day1, dow1, day2))
