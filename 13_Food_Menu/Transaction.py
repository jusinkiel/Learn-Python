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
    id = None

    while id != 'exit':
        clearscreen()
        print_saved_menu()
        id = input("Identifier Number : ")

        if id == 'exit':
            return tmp_ary

        choosen_food, choosen_price = get_food_menu(int(id))

        print("You choose : ", choosen_food)
        print("Price      : ", choosen_price)

        amt = int(input("Amount of Food : "))
        total_price = choosen_price * amt
        print("Total      : ", total_price)
        
        tmp_ary.append([choosen_food, choosen_price, amt, total_price])
        # tmp_ary[0] = food name
        # tmp_ary[1] = food price
        # tmp_ary[2] = food qty
        # tmp_ary[3] = qty * price

    return tmp_ary


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
        orders = taking_order()

        grand_total = sum([i[3] for i in orders])
        print("Your total order is ", grand_total)
        
        print("- " * 35)
        print ("Food Menu".ljust(40) + "Price".ljust(10) + "Amt".ljust(10) + "Total".ljust(10))
        print("- " * 35)
        for item in orders:
            # item = [choosen_food, choosen_price, amt, total_price]
            choosen_food = item[0]
            price = str(item[1])
            amt = str(item[2])
            total_price = str(item[3])

            print(choosen_food.ljust(40) + price.ljust(10) + amt.ljust(10) + total_price.ljust(10))
        print("- " * 35)
        print("Grand Total".rjust(40) + " " * 20 + str(grand_total).ljust(10))

        print(" " * 60 + str(grand_total).ljust(10))
        # print (choosen_food.ljust(20) + str(price).ljust(5))


    else:
        break

    input("Press enter to continue")




