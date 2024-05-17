import os 

def print_saved_menu():
    with open('food.txt') as file:
        for index, text in enumerate(file.readlines()):
            print("{id} | {menu}".format(id=index, menu=text), 
                  end='')
            
def clearscreen():
    os.system("clear")

def get_food_menu(index):
    file = open('food.txt')
    tmp_ft = file.readlines()[index]  # Soup - 9\n
    file.close()

    # 0 = Soup
    # 1 = 9\n 
    tmp_value = tmp_ft.split('-')

    # 0 = 9
    # 1 = ''
    tmp_price = tmp_value[1].split('\n')

    return tmp_value[0], int(tmp_price[0])

def taking_order():
    tmp_ary = []

    id = input("Identifier Number : ")
    amt = input("Amount of Food : ")

    choosen_food, choosen_price = get_food_menu(int(id))
    print(choosen_food, choosen_price)

while True:
    clearscreen()
    print ("Options")
    print ("1. Print Saved Menu")
    print ("2. Taking Order")
    print ("3. Exit")
    
    menu = input ("Choose option: ")

    if menu == '1':
        print_saved_menu()

    elif menu == '2':
        print_saved_menu()
        taking_order()

    else:
        break

    input("Press enter to continue")




