# 오픈 시계

A, B = map(int, input().split())
C = int(input())

minute = (B + C) % 60
hour = A + (B + C) // 60

if hour > 23:
    hour = hour - 24

print(hour, minute)