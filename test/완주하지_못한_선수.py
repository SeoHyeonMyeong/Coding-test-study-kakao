def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in range(len(participant)):
        person = participant.pop()
        if len(participant)==0:
            return person
        if person != completion.pop():
            return person
