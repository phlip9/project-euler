from datetime import timedelta, date

def date_gen(cur, lim):
    while cur < lim:
        cur += timedelta(days=1)
        yield cur

print(len([d for d in date_gen(date(1901, 1, 1), date(2000, 12, 31)) if d.day == 1 and d.weekday() == 6]))

# 171
