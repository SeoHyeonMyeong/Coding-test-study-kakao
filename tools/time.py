from datetime import datetime, time

hour, min = input().split()
hour = int(hour)
min = int(min)
min2 = int(input())

ans = min + min2 + hour * 60
h = ans // 60 % 24
m = ans % 60

print(f"{h} {m}")