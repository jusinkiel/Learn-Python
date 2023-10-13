# Library or API 
import datetime

current = datetime.datetime.now()
print(current)

current_year = int(current.strftime("%Y"))
print("Current Year : {}".format(current_year))


if current_year % 400 == 0:
    print('leap year')
elif current_year % 100 == 0:
    print('not leap year')
elif current_year % 4 == 0:
    print ('leap year')
else:
    print ('not leap year')