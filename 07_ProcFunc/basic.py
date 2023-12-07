# Procedure 
# Function -> but it has a return value

# Parameters -> the things that we need to provide befoire we can run the proc/func
# def balblabla(param1, param2, param3, ...)

# Function to detect a leap year
# Return True, if the year is a leap year
def check_is_a_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
    
def check_is_a_leap_year2():
    year = int(input("Year to check : "))
    if year % 400 == 0:
        return "Leap year"
    elif year % 100 == 0:
        return "Not leap year"
    elif year % 4 == 0:
        return "Leap year"
    else:
        return "Not leap year"

def main():
    
    result = check_is_a_leap_year2()
    print(result)

if __name__ == '__main__':
    main()