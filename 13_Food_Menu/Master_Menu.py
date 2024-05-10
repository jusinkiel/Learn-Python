# Menu
# 1. Add new Menu -> saved into menu.txt
# 2. Print saved menu

def add_new_menu():
    rda = open('food.txt', 'a')
    name = input("Food Name : ")
    price = input("What is price? : ")

    print("{menu_name} - {menu_price}".format(
        menu_name = name, 
        menu_price = price), 
        file=rda)
    # rda.write(choose + "\n")
    rda.close()

def print_saved_menu():
    with open('food.txt') as file:
        for line in file.readlines():
            print(line, end='')

while True:
    print("Master Menu Options")
    print("1. Add New Menu")
    print("2. Print Saved Menu")
    print("3. Edit Menu")
    print("4. Exit")

    menu = input("Choose option : ")

    if menu == '1':
        add_new_menu()
        print_saved_menu()

        with open('food.txt') as file:
            for line in file.readlines():
                print(line, end='')
    
    elif menu == '2':
        print_saved_menu()

        with open('food.txt') as file:
            for line in file.readlines():
                print(line, end='')

    elif menu == '3': 
        exit()

    else:
        break 


    

    
