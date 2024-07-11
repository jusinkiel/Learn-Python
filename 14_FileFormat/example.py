import json

file = open('food.json')

foods = json.load(file)

food_name_key = 'foodName'

for i in foods:
    print(i[food_name_key], 
          'price is', i['price'])


file.close()