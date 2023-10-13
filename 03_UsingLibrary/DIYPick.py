import datetime
from pick import pick

def main():
    while True:
        title = "---- Leap Year Program ----"
        options = [
            '1. Manual Input', 
            '2. Automatically Detect Current Year',  
            '3. Exit'
        ]
        choosen_menu, index_choosen = pick(options, title)
        

        # print("---- Leap Year Program -----")
        # print(" 1. Manual Input")
        # print(" 2. Automatically Detect Current Year")
        # print(" 3. Exit")

        # year = 0

        if index_choosen == 2:
            break

        elif index_choosen == 0:
            year = int(input('Year : '))
                
        elif index_choosen == 1:
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

        input("Press any key to back to menu")

if __name__ == '__main__':
    main()

    print("")
    print("Thankyou for using this program. Byebye")

