# Answer 7

def frequency_sort(items):
    cpt = [items.count(item) for item in items]
    cpt.sort()
    cpt.reverse()
    res = []
    got = []
    for i in cpt:
        for item in items:
            if items.count(item) == i and not item in got:
                for j in range(i):
                    res.append(item)
                got.append(item)
    return res

# Answer 8

def time_converter(time):
    if len(time) == 9:
        if 'a' in time:
            time = '0' + time[:4]
        else:
            time = str(int(time[0]) + 12) + time[1:4]
    elif 'a' in time and time[:2] == '12':
            time = '0' + str(int(time[:2]) - 12) + time[2:5]
    else:
        if ('p' in time and time[:2] == '12') or ('a' in time): 
            time = time[:5]
        else:
            time = str(int(time[:2]) + 12) + time[2:5]
    return time
    