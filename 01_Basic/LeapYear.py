year = input('number: ')
print('input ' + year)

year2 = int(year)
print(type(year2))
      
if year2 % 400 == 0:
    print('leap year')  
elif year2 % 100 == 0:
    print('not leap year')
elif year2 % 4 == 0:
    print('leap year')
else:
    print('not leap year')