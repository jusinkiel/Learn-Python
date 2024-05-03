# Menu
# 1. Add new Menu -> saved into menu.txt
# 2. Print saved menu

while True:
    print("Master Menu Options")
    print("1. Add New Menu")
    print("2. Print Saved Menu")
    print("3. Exit")

    menu = input("Choose option : ")

    if menu == '1':
        rda = open('food.txt', 'a')
        choose = input("Choose food : ")
        print(choose, file= rda)
        # rda.write(choose + "\n")
        rda.close()
    
    elif menu == '2':
        with open('food.txt') as file:
            for line in file.readlines():
                print(line, end='')

    elif menu == '3': 
        exit()

    else:
        break 


    

    
