'''
1. Insert Menu
     - Choose category --> Food or Meal
     - If Food 
       - Ask for food name
       - Ask for the price

     - If Meal
     - If Food 
       - Ask for food name
       - Ask for the price
       - Ask for multiple contents
  
2. Print Menu
'''

import json
import os

def Add_Menu():

    foods = [] # initial array len(foods) = 0

    if os.path.exists('food.json') and os.path.getsize('food.json'):
        file = open('food.json', 'r') 
        foods = json.load(file)
        file.close()

    print("1. Foods")
    print("2. Meals")

    fm = input("Choose option : ")

    new_id = 1
    if foods != None and len(foods) > 0:
        new_id = foods[-1]['id'] + 1

    if fm == '1':
        name = input("Food Name : ")
        price = int(input("Food Price : "))

        foods.append({
            "id": new_id,
            "category": "food", 
            "foodName": name, 
            "price": price
        })

    elif fm == '2':
        name = input("Meal  Name : ")
        price = int(input("Meal Price : "))

        dd = []
        tp = None 

        while tp != 'exit':
            tp = input("Contents : ")

            # Option 1
            if tp == 'exit':
                break

            dd.append(tp)

            # Option 2
            # if tp != 'exit': 
            #     dd.append(tp)
            # else:
            #     break

        foods.append({
            "id": new_id,
            "category": "meal", 
            "foodName": name, 
            "price": price,
            "contents": dd
        })


    file = open('food.json', 'w')
    json.dump(foods, file, indent=4)
    file.close()


while True:
    print("Master_Menu_Options")
    print("1. Add Menu")
    print("2. Print Menu")
    print("3. Exit")

    menu = input("Choose option : ")

    if menu == '1':
        Add_Menu()

    else:
        break

    os.system("clear")

input("Press enter to continue")