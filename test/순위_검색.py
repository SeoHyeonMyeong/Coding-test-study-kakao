def solution(info, query):

    data = dict()
    for line in info:
        line = line.split(" ")
        for a1 in set(["-",line[0]]):
            for a2 in set(["-",line[1]]):
                for a3 in set(["-",line[2]]):
                    for a4 in set(["-",line[3]]):
                        key = a1+a2+a3+a4
                        if key in data.keys():
                            data[key].append(int(line[4]))
                        else:
                            data[key] = [int(line[4])]

    for key in data.keys():
        data[key].sort()

    ans = []
    for q in query:
        q = q.split(" and ")
        q = q + q.pop().split(" ")
        key = q[0]+ q[1] + q[2] + q[3]
        value = int(q[4])
        if not key in data:
            ans.append(0)
        else:
            lst = data[key]
            ans.append(len(lst) - binary_search(value,0,len(lst),lst))
    
    return ans

def binary_search(target, start, end, data):
    if start> end:
        return 0
    if start == end:
        return end
    mid = (start + end) // 2

    if (data[mid] >= target):
        if mid == 0:
            return mid
        elif data[mid-1] < target:
            return mid
        else:
            end = mid - 1
    else:
        start = mid + 1
    return binary_search(target,start,end,data)

# info = []
# query = []
# for a1 in ["-","java","python","cpp"]:
#     for a2 in ["-","backend","frontend"]:
#         for a3 in ["-","junior","senior"]:
#             for a4 in ["-","pizza","chicken"]:
#                 key = a1 + " and " + a2 + " and " + a3 + " and " + a4 + " 10"
#                 query.append(key)
# for a1 in ["-","java","python","cpp"]:
#     for a2 in ["-","backend","frontend"]:
#         for a3 in ["-","junior","senior"]:
#             for a4 in ["-","pizza","chicken"]:
#                 key = a1 + " " + a2 + " " + a3 + " " + a4 + " 5"
#                 info.append(key)

# print(solution(info,query))

