def solution(s):
    list = []
    if len(s) % 2 == 0:
        first = 0
        second = 2
        while second <= len(s):
            list.append(s[first:second])
            first += 2
            second += 2
    else:
        first = 0
        second = 2
        while second <= len(s)-1:
            list.append(s[first:second])
            first += 2
            second += 2
        list.append(s[-1] + "_")

    return list


print(solution("salfalflakfakfa"))
