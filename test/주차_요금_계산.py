import datetime
import math

def process_time(time1, time2):
    global timestamp
    dateformat = "%H:%M"
    time1 = datetime.datetime.strptime(time1,dateformat)
    time2 = datetime.datetime.strptime(time2,dateformat)
    diff = datetime.timedelta(
        hours = time2.hour - time1.hour,
        minutes = time2.minute - time1.minute
    )
    return diff.seconds//60

def solution(fees, records):
    default_time = fees[0]
    default_price = fees[1]
    d_time = fees[2]
    d_price = fees[3]

    cars = dict()
    ans = dict()

    for record in records:
        record = record.split(" ")
        if record[2] == "IN":
            cars[record[1]] = record[0]
        elif record[2] == "OUT":
            time = process_time(cars[record[1]],record[0])
            del cars[record[1]]
            if record[1] in ans:
                ans[record[1]] += time
            else:
                ans[record[1]] = time
    for car in cars.keys():
        time = process_time(cars[car],"23:59")
        if car in ans:
            ans[car] += time
        else:
            ans[car] = time

    result = []
    for item in sorted(ans):
        time = ans[item]
        if time <= default_time:
            time = default_time
        fee = default_price + math.ceil((time - default_time) / d_time) * d_price
        result.append(fee)
    # ans = default_price + (time - default_time) / d_time * d_price

    return result


# fees = [180, 5000, 10, 600]
# records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]	
# print(solution(fees,records))

# print(process_time("06:00","06:34"))