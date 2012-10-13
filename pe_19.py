from datetime import timedelta, date

cur = date(1901, 1, 1)
end = date(2000, 12, 31)

num_sundays = 0

while cur <= end:
	if cur.day == 1 and cur.weekday() == 6:
		print(cur)
		num_sundays += 1
	cur += timedelta(days = 1)

print("Sundays on 1st of month from 1900-1-1 to 2000-12-31:", num_sundays)

# 171