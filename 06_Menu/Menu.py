def rectangle1(length):
    for row in range(0, length):
        for col in range(0, length):
            if row == 0 or col == 0 or row == length - 1 or col == length -1:
                print('*', end=' ')
            elif col == row:
                print ('*', end=' ')
            elif row == length - 1 - col:
                print  ('*', end=' ')
            else:
                print(' ', end=' ')
                
        print('')

def rectangle2(length):
    for row in range(0,length):
        for col in range(0, length):
            if (row + col) % 2 == 0:
                print('-', end=' ')
            else:
                print('|', end=' ')
            
        print ('')

def Triangle(length):
    max_number = 1
    for row in range (0, length):  
        for col in range (0, max_number):
            print('x', end=' ')
        max_number = max_number + 1 


        print ('')

def main():
    while True:
        print("-----Shapes----")
        print("1. Rectangle 1")
        print("2. Rectabgle 2")
        print("3. Triangle")
        print("4. Exit")

        menu = input("Choose shape : ")

        tmp_length = int(input("Length : "))  

        if menu == '1':
            rectangle1(tmp_length)

        elif menu == '2':
            rectangle2(tmp_length) 

        elif menu == '3':
            Triangle(tmp_length) 

        else:
            break

        print("blablabla")


if __name__ == '__main__':
    main()