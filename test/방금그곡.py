import datetime

m = "ABCDEFG"
musicinfos = ["11:00,15:14,HELLO,CDEFGAB", "03:00,13:05,WORLD,ABCD#EF#"]

pitch_code = ["C","C#","D","D#","E","E#","F","F#","G","G#","A","A#","B"]
new_code = ["0","1","2","3","4","5","6","7","8","9","A","B","C"]

def encode_pitch(pitch):
    code = []
    for i in range(len(pitch)):
        if pitch[i] == "#":
            continue
        elif i == len(pitch)-1:
            code.append(pitch_code.index(pitch[i]))
        elif pitch[i+1] == "#":
            code.append(pitch_code.index(pitch[i:i+2]))
        else:
            code.append(pitch_code.index(pitch[i]))
    ans = ""
    for i in code:
        ans += new_code[i]
    return ans

def recog_music(musics):
    objects = []
    for item in musics:
        object = item.split(',')
        object[3] = encode_pitch(object[3])
        objects.append(object)
    return objects

def diff_min(time_1,time_2):
    dateformat = "%H:%M"
    time_1 = datetime.datetime.strptime(time_1,dateformat)
    time_2 = datetime.datetime.strptime(time_2,dateformat)
    diff = int((time_2 - time_1).seconds/60)
    return diff

def solution(m,musicinfos):
    objects = recog_music(musicinfos)
    arr = []
    ans = ""
    m = encode_pitch(m)
    for i in objects:
        min = diff_min(i[0],i[1])
        n = len(i[3]);
        music = i[3] * int(min/n) + i[3][0:min%n]
        if music.find(m)>=0:
            arr.append([i[2],min])
    if len(arr) ==0:
        return "(None)"
    else:
        arr.sort(reverse=True,key=lambda x:x[1])
        return arr[0][0]
# print(recog_music(musicinfos))
# print(diff_min("16:33","18:36"))
# print(encode_pitch("CC#E"))
# print(decode_pitch([0,1,4]))
print(solution(m,musicinfos))