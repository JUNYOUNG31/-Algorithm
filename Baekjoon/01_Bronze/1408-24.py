# 24

hour1, min1, sec1 = map(int, input().split(':'))
hour2, min2, sec2 = map(int, input().split(':'))
time = (hour2 * 3600) + (min2 * 60) + sec2 - ((hour1 * 3600) + (min1 * 60) + sec1)
if time < 0:
    time += 60 * 60 * 24
hour = time // 3600
min = (time % 3600) // 60
sec = time % 60
print("%02d:%02d:%02d" % (hour, min, sec))
