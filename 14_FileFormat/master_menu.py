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
    mode = 'r+' if os.path.exists('food.json') else 'w+'
    file = open('food.json', 'w+') # w+ will create a file if the file is not exist

    foods = [] # initial array len(foods) = 0
    print(file.readlines())

    # If the file is exists and not empty file, i will replace foods with the file
    if file != None and len(file.read()) > 0: 
        foods = json.load(file)

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

    if mode == 'r+':
        file.seek(0)

    json.dump(foods, file, indent=4)

    file.truncate()
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

input("Press enter to continue")