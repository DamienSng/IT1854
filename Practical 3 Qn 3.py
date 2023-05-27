time = int(input('enter your time in seconds'))

hours = (time//60)//60

hr_in_sec = hours*60*60

min_left = time - hr_in_sec

mins = min_left // 60

sec_left = min_left % 60

print(time, 'seconds in', hours ,'hours', mins ,'minutes', sec_left,'seconds')
