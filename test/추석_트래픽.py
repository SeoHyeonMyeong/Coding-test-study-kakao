import datetime

timestamp = []

def process_time(time, diff):
    global timestamp
    dateformat = "%H:%M:%S.%f"
    diff = datetime.datetime.strptime(diff,"%S.%f")
    diff = datetime.timedelta(
        seconds = diff.second,
        milliseconds = int(diff.microsecond/1000)-1
    )
    time_2 = datetime.datetime.strptime(time,dateformat)
    time_2 = datetime.timedelta(
        hours = time_2.hour,
        minutes = time_2.minute,
        seconds=time_2.second,
        milliseconds = int(time_2.microsecond/1000)
    )
    time_1 = time_2 - diff
    timestamp.append([time_1,time_2])

def solution(lines):
    for line in lines:
        token = line.split(" ")
        if len(token[2]) ==2:
            token[2] = token[2][:-1] + ".0s" 
        process_time(token[1], token[2][:-1])

    ans = 0
    for time in timestamp:
        temp = 0
        start_time = time[1]
        end_time = time[1] + datetime.timedelta(seconds=1)
        print(end_time)
        for t in timestamp:
            if t[0] < end_time and t[1] >= start_time:
                temp += 1
        if temp >= ans:
            ans = temp
    return ans

# lines = [
#     "2016-09-15 01:00:04.001 2.0s",
#     "2016-09-15 01:00:07.000 2s"
# ]
# print(solution(lines))
# print(timestamp)