from numpy import datetime_as_string


def sortDict(dic):
    temp = {}
    for key in sorted(dic.keys()):
        temp[key] = dic[key]
        
    return temp


def addEvent(schedule, _date, content):
    import datetime

    schedule[datetime.date(year= _date[0], month= _date[1], day= _date[2])] = content
    schedule = sortDict(schedule)

    return schedule