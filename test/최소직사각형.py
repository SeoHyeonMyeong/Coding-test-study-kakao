def solution(sizes):
    width = 0
    height = 0
    for size in sizes:
        size.sort()
        if width < size[0]:
            width = size[0]
        if height < size[1]:
            height = size[1]

    return width * height