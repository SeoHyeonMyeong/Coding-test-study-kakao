def solution(files):
    object = []
    for file in files:
        head = ''
        head_end = False
        number = ''
        number_end = False
        tail = ''
        for char in file:
            if not head_end:
                if char.isnumeric():
                    number += char
                    head_end = not head_end
                else:
                    head += char
            elif not number_end:
                if char.isnumeric():
                    number += char
                else:
                    tail += char
                    number_end = not number_end
            else:
                tail += char
        object.append([head,number,tail,file])
    
    object.sort(key=lambda file: (file[0].lower(),int(file[1])))
    _,_,_,files = zip(*object)
    return files

files = ["foo9.txt","foo010bar020.zip","F-15"]
print(solution(files))
