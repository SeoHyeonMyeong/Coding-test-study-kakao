def solution(files):
    for file in files:
        head = ''
        head_end = False
        number = ''
        number_end = False
        tail = ''
        for char in file:
            if head_end:
                
