import datetime
while True:
    print("---- Leap Year Program -----")
    print(" 1. Manual Input")
    print(" 2. Automatically Detect Current Year")
    print(" 3. Exit")

    menu = input("Choose the menu : ")
    # year = 0

    if menu == '3':
        break

    elif menu == '1':
        year = int(input('Year : '))
            
    elif menu == '2':
        current = datetime.datetime.now()
        year = int(current.strftime("%Y"))
        print("Current Year : {}".format(year))

# Check 'year' variable 
if year % 400 == 0:
    print('leap year')
elif year % 100 == 0:
    print('not leap year')
elif year % 4 == 0:
    print ('leap year')
else:
    print ('not leap year')

print("")

print("")
print("Thankyou for using this program. Byebye")

