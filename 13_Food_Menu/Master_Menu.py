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
        for index, text in enumerate(file.readlines()):
            print("{id} | {menu}".format(id=index, menu=text), 
                  end='')


# Create a new procedure for update data
# Ask which index taht u want to upd
# Input new menu 
# Input new pricing
# Save it 
def update_menu():
    print_saved_menu()

    id = input("Identifier Number : ")
    new = input("New Item Name : ")
    prce = input ("New Price : ")

    data = []
    with open('food.txt') as file:
        for index, text in enumerate(file.readlines()):
            if str(index) != id:
                data.append(text) # Take the original data
            else: #index == id, take teh data based on user input
                data.append("{menu_name} - {menu_price}\n".format(
                    menu_name = new, 
                    menu_price = prce))
                
    # data = [
    #     'chicken-15',
    #     'xxx-1',
    #     'yyy-2'
    # ]

    rda = open('food.txt', 'w')
    for text in data:
        print(text, file=rda, end='')
    rda.close()

            

while True:
    print("Master Menu Options")
    print("1. Add New Menu")
    print("2. Print Saved Menu")
    print("3. Edit Menu")
    print("4. Delete Menu")
    print("5. Exit")

    menu = input("Choose option : ")

    if menu == '1':
        add_new_menu()
        print_saved_menu()
    
    elif menu == '2':
        print_saved_menu()


    elif menu == '3': 
        update_menu()

    else:
        break 


    

    
